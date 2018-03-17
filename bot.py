#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time

from src import InstaBot
from src.check_status import check_status
from src.feed_scanner import feed_scanner
from src.follow_protocol import follow_protocol
from src.unfollow_protocol import unfollow_protocol

bot = InstaBot(
    login="",
    password="",
    like_per_day=3000,
    comments_per_day=1000,
    tag_list=['pic', 'picture', 'picoftheday', 'photo', 'photography', 'photographie',
                'sony', 'sonyimages', 'sonyimage', 'sonyalpha', 'sonyalphaa6000', 'sonyalpha6000',
                'sonya6000', 'sonya6300', 'sonya36500', 'sonyalphaclub', 'sonyalpha6000club', 'sonyalphaclubs',
                'sonyalphagang', 'sonycollective', 'sonyalphagallery', 'streetphotography', 'nightphotography',
                'asto', 'astrophoto', 'astrophotography', 'astro_photography_', 'astro_photography',
                'sonya7riii', 'sonya7rii', 'sonya7ii', 'sonya7', 'sonyphotography', 'sony_shots', 'sonyalphasclub',
                'sonyphotogallery', 'sonymirrorless', 'sonyalphaphotos', 'sonypictures', 'sonyphotographer',
                'milkyway', 'milky_way', 'milkywaychasers', 'milkywaygalaxy', 'milkyway_nightscapes', 'milkywayphotography',
                'milkywaypics', 'milkywaychaser', 'milkywayphoto', 'milkywaystarts', 'street', 'streetlight', 'street_vision', 'street_photo_club',
                'streetphotography_bw', 'streetview', 'landscape', 'landscapes', 'landscape_captures', 'landscape_lovers', 'landscapephotography',
                'landscapelover', 'landscapelovers', 'landscaping', 'landscape_photography', 'landscape_panorama'],
    max_like_for_one_tag=100,
    follow_per_day=1000,
    follow_time=5 * 60 * 60,
    unfollow_per_day=1000,
    unfollow_break_min=15,
    unfollow_break_max=30,
    log_mod=0,
    # List of list of words, each of which will be used to generate comment
    # For example: "This shot feels wow!"
    comment_list=[["this", "the", "your"],
                  ["photo", "picture", "pic", "shot", "snapshot"],
                  ["is", "looks", "feels"],
                  ["great", "super", "good", "cool", "so cool",
                   "very cool", "stylish", "so stylish", "excellent",
                    "amazing"],
                  ["!", "!!", "!!!", "🙂", "👍", "💪", "👌", "😀", "👏"]],
    # Use unwanted_username_list to block usernames containing a string
    ## Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
    ### 'free_followers' will be blocked because it contains 'free'
    unwanted_username_list=[
        'free', 'follow', 'follower', 'gain', '.id', '_id'
    ])
while True:

    #print("# MODE 0 = ORIGINAL MODE BY LEVPASHA")
    #print("## MODE 1 = MODIFIED MODE BY KEMONG")
    #print("### MODE 2 = ORIGINAL MODE + UNFOLLOW WHO DON'T FOLLOW BACK")
    #print("#### MODE 3 = MODIFIED MODE : UNFOLLOW USERS WHO DON'T FOLLOW YOU BASED ON RECENT FEED")
    #print("##### MODE 4 = MODIFIED MODE : FOLLOW USERS BASED ON RECENT FEED ONLY")
    #print("###### MODE 5 = MODIFIED MODE : JUST UNFOLLOW EVERYBODY, EITHER YOUR FOLLOWER OR NOT")

    ################################
    ##  WARNING   ###
    ################################

    # DON'T USE MODE 5 FOR A LONG PERIOD. YOU RISK YOUR ACCOUNT FROM GETTING BANNED
    ## USE MODE 5 IN BURST MODE, USE IT TO UNFOLLOW PEOPLE AS MANY AS YOU WANT IN SHORT TIME PERIOD

    mode = 0

    #print("You choose mode : %i" %(mode))
    #print("CTRL + C to cancel this operation or wait 30 seconds to start")
    #time.sleep(30)

    if mode == 0:
        bot.new_auto_mod()

    elif mode == 1:
        check_status(bot)
        while bot.self_following - bot.self_follower > 200:
            unfollow_protocol(bot)
            time.sleep(10 * 60)
            check_status(bot)
        while bot.self_following - bot.self_follower < 400:
            while len(bot.user_info_list) < 50:
                feed_scanner(bot)
                time.sleep(5 * 60)
                follow_protocol(bot)
                time.sleep(10 * 60)
                check_status(bot)

    elif mode == 2:
        bot.bot_mode = 1
        bot.new_auto_mod()

    elif mode == 3:
        unfollow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 4:
        feed_scanner(bot)
        time.sleep(60)
        follow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 5:
        bot.bot_mode = 2
        unfollow_protocol(bot)

    else:
        print("Wrong mode!")
