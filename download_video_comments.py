#!/usr/bin/python

import os
import json
from itertools import islice
import requests


class DownloadYouTubeVideoComments(object):
    """
    Class that implements all the required methods to download the comments of YouTube Videos leveraging the YouTube Data APIv3.
    The class uses the 'commentThreads' endpoint of YouTube Data API to retrieve the comments. Check here for more options
    regarding the use of this endpoint: https://developers.google.com/youtube/v3/docs/commentThreads/list
    """
    def __init__(self, API_KEY='AIzaSyASojqluEFOuAapb3qQhC3Yrsz8EYKhxhk'):
        # BASE DIRECTORIES and PATHS
        self.VIDEO_COMMENTS_BASE_DIR = 'data/youtube_videos/comments/'

        # YOUTUBE DATA API Paramaters
        self.YOUTUBE_DATA_API_KEY = API_KEY

        # Other Parameters
        self.COMMENTS_ATTRIBUTES = 'id%2Csnippet%2Creplies'  # the attributes to be retrieved for each comment
        self.COMMENTS_ORDER = 'relevance'  # 'time' (Comment threads are ordered by time) or 'relevance' (Comment threads are ordered by relevance/priority)
        return

    @staticmethod
    def key_exists(element, *keys):
        """
        Check if *keys (nested) exists in `element` (dict).
        :param keys:
        :return: True if key exists, False if not
        """
        if type(element) is not dict:
            raise AttributeError('keys_exists() expects dict as first argument.')
        if len(keys) == 0:
            raise AttributeError('keys_exists() expects at least two arguments, one given.')

        _element = element
        for key in keys:
            try:
                _element = _element[key]
            except KeyError:
                return False
        return True

    def video_comments_exist(self, video_id):
        """
        Method that checks if the comments of a given video has already been downloaded
        :param video_id:
        :return:
        """
        if os.path.isfile('{}{}/{}.json'.format(self.VIDEO_COMMENTS_BASE_DIR, video_id[:3], video_id)):
            return True
        else:
            return False

    @staticmethod
    def write_video_comments(filename, comments_json):
        """
        Method that writes the provided comments in the given filename
        :param filename: The file to append the given comments
        :param comments_json: the comments in JSON format to be written in the file
        :return: None
        """
        with open(file=filename, mode="a", encoding='utf-8') as f:
            # Check if there are any comments
            try:
                for js in comments_json['items']:
                    f.write(json.dumps(js) + ',' + '\n')
            except KeyError:
                return

    def read_video_comments(self, video_id, include_replies=True):
        """
        Method that returns a list with all the downloaded comments files of the given YouTube Video
        :param video_id: the ID of the video to get its comments
        :param include_replies: denotes whether we want to also include the replies in the returned comments array
        :return: a list with the comments of the requested video
        """
        # Initialiaze Variables
        video_comments = list()
        video_comments_filename = '{}{}/{}.json'.format(self.VIDEO_COMMENTS_BASE_DIR, video_id[:3], video_id)

        comment_thread_json_string = '{"all_comments":['

        # Read file if not empty
        if os.path.isfile(video_comments_filename) and os.stat(video_comments_filename).st_size > 0:
            with open(file=video_comments_filename, mode='r', encoding='utf-8') as file:
                comments_cntr = 0
                while True:
                    # Read next N comments (lines in file)
                    next_n_comments = list(islice(file, 50000))
                    # Check if it is the end of file
                    if not next_n_comments:
                        break

                    for comment_line in next_n_comments:
                        if comments_cntr == 0:
                            comment_thread_json_string += comment_line
                        else:
                            comment_thread_json_string += "," + comment_line
                        comments_cntr += 1

                # Convert comments string to json
                comment_thread_json_string += ']}'
                comments_data = json.loads(comment_thread_json_string)

                # Iterate each top level comment threat
                for top_level_comment_threat in comments_data['all_comments']:
                    # video_comments.append(dict(top_level_comment_threat))
                    # Add Top Level Comment
                    video_comments.append(dict(top_level_comment_threat['snippet']['topLevelComment']))

                    # Check if there are any reply comments and add them too
                    if include_replies:
                        if top_level_comment_threat['snippet']['totalReplyCount'] > 0 and self.key_exists(top_level_comment_threat, 'replies', 'comments'):
                            for reply_comment in top_level_comment_threat['replies']['comments']:
                                video_comments.append(dict(reply_comment))
        return video_comments

    def get_comments_page(self, video_id, nextPageToken):
        """
        A function that takes as parameters a Video ID and the pageToken to download
        and request for the
        output: JSON returns the json object of the response TOKEN returns the next page token in order to repeat the process
        QUOTA COST: 4 * 2 = 8 maximum per video
        :param videoId:
        :param API_KEY:
        :param nextPageToken:
        :return:
        """
        URL = "https://www.googleapis.com/youtube/v3/commentThreads?pageToken={}&part={}&maxResults=100&order={}&videoId={}&key={}".format(
            nextPageToken,
            self.COMMENTS_ATTRIBUTES,
            self.COMMENTS_ORDER,
            video_id,
            self.YOUTUBE_DATA_API_KEY
        )
        response = requests.get(URL, stream=True)
        return response

    def download_video_comments(self, video_id, comments_pages_threshold):
        """
        Method that downloads the comments of a given YouTube Video ID
        :param video_id: the ID of the video to download its comments
        :param comments_pages_threshold: the number of pages to download from the available video's comments.
                                         Each comments page includes a maximum of 100 comments
        :return:
        """
        video_comments_dir = '{}{}'.format(self.VIDEO_COMMENTS_BASE_DIR, video_id[:3])

        # First check if comments already exist
        if not os.path.isfile('{}/{}.json'.format(video_comments_dir, video_id)):
            print('--- [VIDEO: {}] DOWNLOADING VIDEO COMMENTS'.format(video_id))
            # Create Comments base dir if needed
            original_umask = os.umask(0)
            try:
                if not os.path.exists(video_comments_dir):
                    os.makedirs(video_comments_dir, 0o777)
            finally:
                os.umask(original_umask)

            # Download Video Comments
            comment_pages_cntr = 0
            nextPageToken = ''
            while True:
                # Download comments with the specific pageToken
                comments_raw = self.get_comments_page(video_id=video_id, nextPageToken=nextPageToken)
                comments_json = comments_raw.json()
                if 'nextPageToken' not in comments_json:
                    nextPageToken = ''
                else:
                    nextPageToken = comments_json["nextPageToken"]

                # Create files while you still get http responses
                filename = "{}/{}.json".format(video_comments_dir, video_id)
                self.write_video_comments(filename=filename, comments_json=json.loads(comments_raw.text))

                comment_pages_cntr += 1
                if comment_pages_cntr > int(comments_pages_threshold) or nextPageToken == '':
                    break
        else:
            print('--- [VIDEO: {}] VIDEO COMMENTS already exists!'.format(video_id))
        return

ids = ["JgEcBdiadms",
    "mQvw5JXXnrQ",
    "rYQgy8QDEBI",
    "gFQNPmLKj1k",
    "Yb6825iv0Vk",
    "WFQRXDqLUHY",
    "atvJwwec_2A"
    ]
a = DownloadYouTubeVideoComments()

for i in ids:
    a.download_video_comments(i, 20)