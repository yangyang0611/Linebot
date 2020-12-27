import os
import json

from linebot import LineBotApi, WebhookParser
from linebot.models import *


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
line_bot_api = LineBotApi(str(channel_access_token))


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


def send_go_to_menu_button(reply_token):
    confirm_template = TemplateSendMessage(
        alt_text="Are you lost?",
        template=ConfirmTemplate(
            text="是否回去主選單呢？",
            actions=[
                MessageTemplateAction(
                    label="YES!",
                    text="Menu"
                ),
                MessageTemplateAction(
                    label="你沒得選",
                    text="Menu"
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, confirm_template)
    return "OK"

# send video


def send_video(reply_token, vid_url, image):
    video_message = VideoSendMessage(
        original_content_url=vid_url,
        preview_image_url=image
    )

    line_bot_api.reply_message(reply_token, video_message)

    return "OK"

# send info


def send_info(reply_token, word, information, current, brand):
    line_bot_api.reply_message(reply_token,
                               FlexSendMessage(
                                   "Information",
                                   {
                                       "type": "bubble",
                                       "body": {
                                           "type": "box",
                                           "layout": "vertical",
                                           "contents": [
                                               {
                                                   "type": "text",
                                                   "text": word,
                                                   "weight": "bold",
                                                   "size": "xxl",
                                                   "margin": "md"
                                               },
                                               {
                                                   "type": "separator",
                                                   "margin": "xl"
                                               },
                                               {
                                                   "type": "box",
                                                   "layout": "vertical",
                                                   "contents": [
                                                       {
                                                           "type": "text",
                                                           "text": information,
                                                           "wrap": True,
                                                       },
                                                   ],
                                                   "spacing": "sm",
                                                   "margin": "xxl"
                                               },
                                               {
                                                   "type": "separator",
                                                   "margin": "xxl"
                                               },
                                               {
                                                   "type": "text",
                                                   "text": "Where do you want to go?",
                                                   "size": "sm",
                                                   "wrap": True,
                                                   "margin": "xxl"
                                               },
                                               {
                                                   "type": "button",
                                                   "action": {
                                                       "type": "message",
                                                       "label": "Menu",
                                                       "text": "Menu"
                                                   },
                                                   "height": "sm"
                                               },
                                               {
                                                   "type": "button",
                                                   "action": {
                                                       "type": "message",
                                                       "label": brand,
                                                       "text": brand
                                                   },
                                                   "height": "sm"
                                               },
                                               {
                                                   "type": "button",
                                                   "action": {
                                                       "type": "message",
                                                       "label": current,
                                                       "text": current
                                                   },
                                                   "height": "sm"
                                               },
                                           ]
                                       },
                                       "styles": {
                                           "footer": {
                                               "separator": True
                                           }
                                       }
                                   }
                               )
                               )
    return "OK"

# send info 2


def send_info_2(reply_token, word, information, current, brand, series):
    line_bot_api.reply_message(reply_token,
                               FlexSendMessage(
                                   "Information",
                                   {
                                       "type": "bubble",
                                       "body": {
                                           "type": "box",
                                           "layout": "vertical",
                                           "contents": [
                                               {
                                                   "type": "text",
                                                   "text": word,
                                                   "weight": "bold",
                                                   "size": "xxl",
                                                   "margin": "md"
                                               },
                                               {
                                                   "type": "separator",
                                                   "margin": "xl"
                                               },
                                               {
                                                   "type": "box",
                                                   "layout": "vertical",
                                                   "contents": [
                                                       {
                                                           "type": "text",
                                                           "text": information,
                                                           "wrap": True,
                                                       },
                                                   ],
                                                   "spacing": "sm",
                                                   "margin": "xxl"
                                               },
                                               {
                                                   "type": "separator",
                                                   "margin": "xxl"
                                               },
                                               {
                                                   "type": "text",
                                                   "text": "Where do you want to go?",
                                                   "size": "sm",
                                                   "wrap": True,
                                                   "margin": "xxl"
                                               },
                                               {
                                                   "type": "button",
                                                   "action": {
                                                       "type": "message",
                                                       "label": "Menu",
                                                       "text": "Menu"
                                                   },
                                                   "height": "sm"
                                               },
                                               {
                                                   "type": "button",
                                                   "action": {
                                                       "type": "message",
                                                       "label": series,
                                                       "text": series
                                                   },
                                                   "height": "sm"
                                               },
                                               {
                                                   "type": "button",
                                                   "action": {
                                                       "type": "message",
                                                       "label": brand,
                                                       "text": brand
                                                   },
                                                   "height": "sm"
                                               },
                                               {
                                                   "type": "button",
                                                   "action": {
                                                       "type": "message",
                                                       "label": current,
                                                       "text": current
                                                   },
                                                   "height": "sm"
                                               },
                                           ]
                                       },
                                       "styles": {
                                           "footer": {
                                               "separator": True
                                           }
                                       }
                                   }
                               )
                               )
    return "OK"

# send menu


def send_Menu_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="Menu",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="觀光景點",
                    text="工作學習這麽久，是不是該犒賞自己來一趟旅游了呢？🤭",
                    thumbnail_image_url="https://i.imgur.com/oiVnCvn.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="選擇觀光景點",
                            text="觀光景點"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="節日",
                    text="馬來西亞常碰到就節日放假，羡慕吧XD",
                    thumbnail_image_url="https://i.imgur.com/9pV1GlF.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="選擇節日",
                            text="節日"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

# 觀光景點


def send_place_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="Place Menu",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="游樂園",
                    text="該放鬆心情瘋狂尖叫了吧！",
                    thumbnail_image_url="https://i.imgur.com/abO5djB.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="地點介紹",
                            text="游樂園"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="歷史古跡",
                    text="跟著本地人的脚步，一起來看看過去的足跡吧",
                    thumbnail_image_url="https://i.imgur.com/6KZn20I.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="地點介紹",
                            text="歷史古跡"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="回主頁重新選擇請按這",
                    thumbnail_image_url="https://i.imgur.com/cuTMVcx.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="回選單",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

# themepark


def send_themepark_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="Themepark Menu",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="雲頂高原",
                    text="建立在雲端上的樂園？？? 是的，沒錯！",
                    thumbnail_image_url="https://i.imgur.com/DvgNJ0C.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="景點介紹",
                            text="雲頂高原"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="樂高主題樂園",
                    text="童心未泯的大孩子們來看看吧",
                    thumbnail_image_url="https://i.imgur.com/XRwCcBH.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="景點介紹",
                            text="樂高主題樂園"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="回主頁重新選擇請按這",
                    thumbnail_image_url="https://i.imgur.com/cuTMVcx.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="回選單",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"


def send_genting_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="genting_detail",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="雲頂高原景點介紹",
                    text="一起來看看吧~",
                    thumbnail_image_url="https://i.imgur.com/Y83EMs3.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="簡介",
                            text="雲頂高原景點介紹"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="門票及規定",
                    text="學生有折扣，讚吧！須符合條規哦~",
                    thumbnail_image_url="https://i.imgur.com/QBoygDo.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="票價",
                            text="門票及規定"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="雲頂高原影片介紹",
                    text="帶你視覺上更瞭解雲頂高原！",
                    thumbnail_image_url="https://i.imgur.com/HZSihi9.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="影片",
                            text="雲頂高原影片介紹"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="回上一頁",
                    text="回去看看有關游樂園的東東吧",
                    thumbnail_image_url="https://i.imgur.com/x9WRuag.png",
                    actions=[
                        MessageTemplateAction(
                            label="Back",
                            text="游樂園"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="回主頁重新選擇請按這",
                    thumbnail_image_url="https://i.imgur.com/cuTMVcx.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="回選單",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"


def send_legoland_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="legoland_detail",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="樂高主題樂園景點介紹",
                    text="一起來看看吧~",
                    thumbnail_image_url="https://i.imgur.com/Y83EMs3.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="簡介",
                            text="樂高主題樂園景點介紹"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="門票及規定",
                    text="學生有折扣，讚吧！須符合條規哦~",
                    thumbnail_image_url="https://i.imgur.com/QBoygDo.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="票價",
                            text="門票及規定"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="樂高主題樂園影片介紹",
                    text="帶你視覺上更瞭解樂高主題樂園！",
                    thumbnail_image_url="https://i.imgur.com/HZSihi9.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="影片",
                            text="樂高主題樂園影片介紹"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="回上一頁",
                    text="回去看看有關游樂園的東東吧",
                    thumbnail_image_url="https://i.imgur.com/x9WRuag.png",
                    actions=[
                        MessageTemplateAction(
                            label="Back",
                            text="游樂園"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="回主頁重新選擇請按這",
                    thumbnail_image_url="https://i.imgur.com/cuTMVcx.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="回選單",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

# historical_place


def send_historical_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="Historical Menu",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="法摩沙堡",
                    text="看看曾經慘遭荷蘭人和英國人統治的馬來西亞，都剩下些什麽..",
                    thumbnail_image_url="https://i.imgur.com/t9GoAo6.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="法摩沙堡介紹",
                            text="法摩沙堡"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="凱莉古堡",
                    text="凱莉古堡傳説鬧鬼... (′д｀*))━!!!!",
                    thumbnail_image_url="https://i.imgur.com/BfbOeSS.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="凱莉古堡介紹",
                            text="凱莉古堡"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="回主頁重新選擇請按這",
                    thumbnail_image_url="https://i.imgur.com/cuTMVcx.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="回選單",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"


def send_famosa_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="famosa_detail",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="法摩沙堡景點介紹",
                    text="一起來看看吧~",
                    thumbnail_image_url="https://i.imgur.com/Y83EMs3.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="簡介",
                            text="法摩沙堡景點介紹"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="門票及規定",
                    text="要愛惜公物喇，講幾次XD",
                    thumbnail_image_url="https://i.imgur.com/QBoygDo.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="票價",
                            text="門票及規定"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="法摩沙堡影片介紹",
                    text="帶你視覺上更瞭解法摩沙堡！",
                    thumbnail_image_url="https://i.imgur.com/HZSihi9.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="影片",
                            text="法摩沙堡影片介紹"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="回上一頁",
                    text="回去看看有關歷史古跡的東東吧",
                    thumbnail_image_url="https://i.imgur.com/x9WRuag.png",
                    actions=[
                        MessageTemplateAction(
                            label="Back",
                            text="歷史古跡"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="回主頁重新選擇請按這",
                    thumbnail_image_url="https://i.imgur.com/cuTMVcx.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="回選單",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"


def send_Kcastle_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="Kcastle_detail",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="凱利古堡景點介紹",
                    text="一起來看看吧~",
                    thumbnail_image_url="https://i.imgur.com/Y83EMs3.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="簡介",
                            text="凱莉古堡景點介紹"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="門票及規定",
                    text="學生有折扣，讚吧！須符合條規哦~",
                    thumbnail_image_url="https://i.imgur.com/QBoygDo.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="票價",
                            text="門票及規定"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="凱莉古堡影片介紹",
                    text="帶你視覺上更瞭解凱莉古堡！",
                    thumbnail_image_url="https://i.imgur.com/HZSihi9.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="影片",
                            text="凱莉古堡影片介紹"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="回上一頁",
                    text="回去看看有關法歷史古跡的東東吧",
                    thumbnail_image_url="https://i.imgur.com/x9WRuag.png",
                    actions=[
                        MessageTemplateAction(
                            label="Back",
                            text="歷史古跡"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="回主頁重新選擇請按這",
                    thumbnail_image_url="https://i.imgur.com/cuTMVcx.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="回選單",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

# festival


def send_festival_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="Festival Menu",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="華人",
                    text="身爲華人的你，來看看馬來西亞華人過節與台灣有什麽不同吧~",
                    thumbnail_image_url="https://i.imgur.com/aPb7GCc.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="傳統節日",
                            text="華人"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="馬來人",
                    text="馬來人傳統會割包皮，什麽？! \n快點進來瞭解！",
                    thumbnail_image_url="https://i.imgur.com/mJEDl9t.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="傳統節日",
                            text="馬來人"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="印度人",
                    text="我們在這個節日會用刀子刺穿喉嚨，還好這個節日只慶祝一天\n(｡･∀･)ﾉ",
                    thumbnail_image_url="https://i.imgur.com/F5BXAar.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="傳統節日",
                            text="印度人"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="回主頁重新選擇請按這",
                    thumbnail_image_url="https://i.imgur.com/cuTMVcx.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="回選單",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

# 華人


def send_chinese_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="Chinese Menu",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="農曆新年",
                    text="恭喜恭喜，新年快樂！",
                    thumbnail_image_url="https://i.imgur.com/x5A6lFx.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="節日介紹",
                            text="農曆新年"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="端午節",
                    text="爲什麽要把飯包在葉子裏嘛？\n怪透 OuO",
                    thumbnail_image_url="https://i.imgur.com/am8fWru.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="節日介紹",
                            text="端午節"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="回主頁重新選擇請按這",
                    thumbnail_image_url="https://i.imgur.com/cuTMVcx.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="回選單",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"


def send_new_year_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="New year Menu",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="農曆新年由來",
                    text="傳説在很久很久以前，有一個食人怪....",
                    thumbnail_image_url="https://i.imgur.com/Y83EMs3.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="農曆新年由來",
                            text="農曆新年由來"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="農曆新年食物",
                    text="看看華人們在這天都胖幾斤吧。\n不是啦，是看都吃些什麽傳統食物喇",
                    thumbnail_image_url="https://i.imgur.com/V5MNQEW.png",
                    actions=[
                        MessageTemplateAction(
                            label="農曆新年食物",
                            text="農曆新年食物"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="回上一頁",
                    text="回去看看有關華人的節日吧",
                    thumbnail_image_url="https://i.imgur.com/x9WRuag.png",
                    actions=[
                        MessageTemplateAction(
                            label="Back",
                            text="華人"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="回主頁重新選擇請按這",
                    thumbnail_image_url="https://i.imgur.com/cuTMVcx.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="回選單",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

# dragon_boat


def send_dragon_boat_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="Dragon boat Menu",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="端午節由來",
                    text="傳説在很久很久以前，有一個愛國詩人....",
                    thumbnail_image_url="https://i.imgur.com/Y83EMs3.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="端午節由來",
                            text="端午節由來"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="端午節食物",
                    text="看看華人們在這天都胖幾斤吧。\n不是啦，是看都吃些什麽傳統食物吧~",
                    thumbnail_image_url="https://i.imgur.com/l0pSYsQ.png",
                    actions=[
                        MessageTemplateAction(
                            label="端午節食物",
                            text="端午節食物"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="回上一頁",
                    text="回去看看有關華人的節日吧",
                    thumbnail_image_url="https://i.imgur.com/x9WRuag.png",
                    actions=[
                        MessageTemplateAction(
                            label="Back",
                            text="華人"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="回主頁重新選擇請按這",
                    thumbnail_image_url="https://i.imgur.com/cuTMVcx.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="回選單",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"


# 馬來人
def send_malay_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="Malay Menu",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="哈芝節",
                    text="恭喜恭喜，哈芝節快樂！",
                    thumbnail_image_url="https://i.imgur.com/QotkS1Y.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="節日介紹",
                            text="哈芝節"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="開齋節",
                    text="餓了一個月，終於可以吃飯了\n(⊙﹏⊙)",
                    thumbnail_image_url="https://i.imgur.com/gO8jzLY.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="節日介紹",
                            text="開齋節"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="回主頁重新選擇請按這",
                    thumbnail_image_url="https://i.imgur.com/cuTMVcx.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="回選單",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

# haji


def send_haji_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="Haji Menu",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="哈芝節由來",
                    text="傳説在很久很久以前，有一個上蒼....",
                    thumbnail_image_url="https://i.imgur.com/Y83EMs3.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="哈芝節由來",
                            text="哈芝節由來"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="哈芝節食物",
                    text="看看馬來人們在這天都胖幾斤吧。\n不是啦，是看都吃些什麽傳統食物吧~",
                    thumbnail_image_url="https://i.imgur.com/Ai46ibW.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="哈芝節食物",
                            text="哈芝節食物"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="回上一頁",
                    text="回去看看有關游馬來人的節日吧",
                    thumbnail_image_url="https://i.imgur.com/x9WRuag.png",
                    actions=[
                        MessageTemplateAction(
                            label="Back",
                            text="馬來人"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="回主頁重新選擇請按這",
                    thumbnail_image_url="https://i.imgur.com/cuTMVcx.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="回選單",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

# raya


def send_raya_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="Raya Menu",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="開齋節由來",
                    text="傳説在很久很久以前，有一個虔誠的教徒....",
                    thumbnail_image_url="https://i.imgur.com/Y83EMs3.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="開齋節由來",
                            text="開齋節由來"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="開齋節食物",
                    text="看看馬來人們在這天都胖幾斤吧。\n不是啦，是看都吃些什麽傳統食物吧~",
                    thumbnail_image_url="https://i.imgur.com/ZhhebE8.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="開齋節食物",
                            text="開齋節食物"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="回上一頁",
                    text="回去看看有關馬來人的節日吧",
                    thumbnail_image_url="https://i.imgur.com/x9WRuag.png",
                    actions=[
                        MessageTemplateAction(
                            label="Back",
                            text="馬來人"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="回主頁重新選擇請按這",
                    thumbnail_image_url="https://i.imgur.com/cuTMVcx.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="回選單",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

# 印度人


def send_indian_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="Indian Menu",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="屠妖節",
                    text="恭喜恭喜，屠妖節快樂！",
                    thumbnail_image_url="https://i.imgur.com/0Nivoub.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="節日介紹",
                            text="屠妖節"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="大寶森節",
                    text="我們在這天除了被刀子刺穿，還會被棍子刺穿哦，厲害吧👍",
                    thumbnail_image_url="https://i.imgur.com/Cnc7uHc.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="節日介紹",
                            text="大寶森節"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="回主頁重新選擇請按這",
                    thumbnail_image_url="https://i.imgur.com/cuTMVcx.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="回選單",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

# deepa


def send_deepa_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="deepa Menu",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="屠妖節由來",
                    text="傳説在很久很久以前，有一個妖怪們....",
                    thumbnail_image_url="https://i.imgur.com/Y83EMs3.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="屠妖節由來",
                            text="屠妖節由來"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="屠妖節食物",
                    text="看看印度人們在這天都胖幾斤吧。\n不是啦，是看都吃些什麽傳統食物吧~",
                    thumbnail_image_url="https://i.imgur.com/MtdOp7f.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="屠妖節食物",
                            text="屠妖節食物"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="回上一頁",
                    text="回去看看有關印度人的節日吧",
                    thumbnail_image_url="https://i.imgur.com/x9WRuag.png",
                    actions=[
                        MessageTemplateAction(
                            label="Back",
                            text="印度人"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="回主頁重新選擇請按這",
                    thumbnail_image_url="https://i.imgur.com/cuTMVcx.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="回選單",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

# thai


def send_thai_carousel(reply_token):
    carousel_template = TemplateSendMessage(
        alt_text="Thai Menu",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="大寶森節由來",
                    text="傳説在很久很久以前，雪山女神的幼子....",
                    thumbnail_image_url="https://i.imgur.com/Y83EMs3.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="大寶森節由來",
                            text="大寶森節由來"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="大寶森節食物",
                    text="看看印度人們在這天都胖幾斤吧。\n不是啦，是看都吃些什麽傳統食物吧~",
                    thumbnail_image_url="https://i.imgur.com/MtdOp7f.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="大寶森節食物",
                            text="大寶森節食物"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="回上一頁",
                    text="回去看看有關印度人的節日吧",
                    thumbnail_image_url="https://i.imgur.com/x9WRuag.png",
                    actions=[
                        MessageTemplateAction(
                            label="Back",
                            text="印度人"
                        ),
                    ]
                ),
                CarouselColumn(
                    title="Menu",
                    text="回主頁重新選擇請按這",
                    thumbnail_image_url="https://i.imgur.com/cuTMVcx.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="回選單",
                            text="Menu"
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template)

    return "OK"

# fsm


def send_fsm(reply_token):
    line_bot_api.reply_message(
        reply_token,
        ImageSendMessage(
            original_content_url="https://i.imgur.com/zP486SZ.png",
            preview_image_url="https://i.imgur.com/zP486SZ.png",
            quick_reply=QuickReply(items=[QuickReplyButton(
                action=MessageAction(label='Go back to menu', text='Menu'))])
        )
    )
    return "OK"
