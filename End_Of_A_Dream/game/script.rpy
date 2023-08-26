# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define m = Character("mizuki")

define sn = Character("文学少年",color= "#3369cf")

# 游戏在此开始。

default preferences.afm_time = 15
default preferences.text_cps = 30

init python: 
    tcps = 30

    def slow_down():
        global tcps
        tcps = preferences.text_cps
        preferences.text_cps = preferences.text_cps * 0.6

    def set_text_speed( spd ):
        preferences.text_cps = spd

    def recover_speed():
        preferences.text_cps = 30

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    play music "yuuki.mp3" fadein 3.0 fadeout 1.0

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    scene bg sunset
    with fade

    ""
    # 此处显示各行对话。
    "行动力极差"
    "别人这么指责他"
    "他声称"
    "自己要创作一部伟大的作品"
    "从初春到夏末"
    "结果六个月都没写好大纲"
    "每周都有新的想法"
    "每周都没能将其实现"
    "坐在书桌前"
    "中性笔在指尖旋转"
    "目的是什么"
    "意义是什么"
    "思索着, 没有答案"
    ""
    $ slow_down()
    "什么是目的"
    $ slow_down()
    "什么是意义"
    "思绪在如蝉鸣一样单调地震动"
    ""
    $ set_text_speed( 10 )
    "最开始 \n为了什么而创作?"

    "为了抒情青春? \n记录思绪?"
    "都不是"
    $ set_text_speed( 15 )
    "他隐约记得心中有一丝不甘"
    $ slow_down()

    "不甘什么?从何时,何处产生?"
    $ slow_down()  
    "好像回想起了过去"

    $ recover_speed()    
    scene bg sunset vague
    with dissolve
    "如何概述?"

    "记忆甚至不能把事件串成一串"
    "没有前因后果"
    "隐约记得几个人名,和他们恶意的笑"

    "氟西汀对记忆确实有影响"
    sn "不快的事,忘了也罢"

    scene bg sunset
    with dissolve

    "如何概述?"
    "雄竞失败? \n 大概和性别无关,虽然只有一群男生"
    sn "在教室里做题并没有什么雄竞"
    "在高压环境下,崩溃并一蹶不振"
    sn "倒是有很长一段时间什么都不想做"
    "抑或是"
    "在抢位置的现实游戏中被人挤了下去"
    sn "仿佛眼睁睁看着自己沉入水泥,难以呼吸"
    "大概如此"
    $ slow_down()  
    "大概如此"
    $ recover_speed()
    "大风吹着谁 谁就倒霉"
    "大概是风吹到自己头上了吧"
    "他这样想到"

    "到底想要创作什么呢?"
    sn "我到底, 想要什么呢"

    "对身边一切失去兴趣"
    "身边的一切都失去了意义"
    "没有意义"
    sn "没有了主观能动性"
    "于是躲进自己的世界里,假装自己是个意气风发的少年"

    sn "我还有什么可以做的呢"
    "每天编织着自己的梦"
    "用洁白的,温柔的幻想"
    "像蚕蛹一般将自己包围起来"
    "逃避着灰色的现实"

    "实际上脑袋空空,每天重复着外界输入的语句"
    $ set_text_speed( 10 )
    sn "除了幻想，什么也做不到"
    $ slow_down()
    "一事无成"
    $ slow_down()
    "一事无成"
    $ slow_down()
    "一事无成"

    $ recover_speed()

    scene bg sunset
    with fade
    "思维重新缓过来"
    "窗边已是夕阳"
    "桌上的纸写了一半"
    "桌角放着一篇文章"
    "<注意力是你所需要的全部>"
    "大概大部分人类是缺乏注意力的吧"

    sn "我算得上,文学少年吗?"
    "大概文学只是慰藉吧"

    "整理一遍草稿和思绪"
    "重温那些灵感,记录有意思的部分"
    $ slow_down()
    "折成纸飞机"
    "飞向天空"
    "当作留给天空的纪念"
    "末尾"
    "也将自己折成纸飞机"
    "回归天空"
    scene bg sunset
    with fade
    ""
    ""
    ""
    ""
    ""

    return
