# coding:UTF-8
import random
s = ''
for i in range(65,91):
    s += chr(i)
for i in range(97,123):
    s +=chr(i)
for i in range(10):
    s += str(i)
# print(len(s))
# with open('test.txt','w',encoding='utf-8') as f:
#     for i in range(10000):
#         content = ''
#         for j in range(10):
#             ran_str = random.choice(s)
#             content += ran_str
#         f.write(content + '\n')
# f.close()

# with open('test.txt','r',encoding='utf-8') as f:
#     for line in f.readlines():
#         count = 0
#         for var in line:
#             if var.isdigit():
#                 count += 1
#             print(count)
# f.close()

# dic = {}
# for i in range(10):
#     dic[str(i)] = 0
# with open('test.txt','r',encoding='utf-8') as f:
#     for line in f.readlines():
#         for var in line:
#             if var.isdigit():
#                 dic[var] += 1
#     print(dic)
# f.close()

import time
# t = time.localtime()
# print(t)
# t = time.strftime('%y %m %d %H %M %S',time.localtime())
# print(t)
#
#
import datetime
# t1 = datetime.timedelta(hours=24)
# t = datetime.datetime.now()
# t = t+t1
# print(t)
# print(t.date())
# print(t.time())
# print(t.strftime('%yyear%mmonth%dday').replace('year','年').replace('month','月').replace('day','日'))
# import os
# f = os.path.getatime('test.txt')
# print(time.strftime('%y-%m-%d',time.localtime(f)))
#
# f = os.path.getctime('test.txt')
# print(time.localtime(f))
#
# f = os.path.getmtime('test.txt')
# print(time.localtime(f))

f = open('test.txt','a',encoding='utf-8')
str1 = [{"ename":105,"cname":"廉颇","title":"正义爆轰","pay_type":10,"new_type":0,"hero_type":3,"skin_name":"正义爆轰|地狱岩魂"},{"ename":106,"cname":"小乔","title":"恋之微风","new_type":0,"hero_type":2,"skin_name":"恋之微风|万圣前夜|天鹅之梦|纯白花嫁|缤纷独角兽"},{"ename":107,"cname":"赵云","title":"苍天翔龙","new_type":0,"hero_type":1,"hero_type2":4,"skin_name":"苍天翔龙|忍●炎影|未来纪元|皇家上将|嘻哈天王|白执事|引擎之心"},{"ename":108,"cname":"墨子","title":"和平守望","new_type":0,"hero_type":2,"hero_type2":3,"skin_name":"和平守望|金属风暴|龙骑士|进击墨子号"},{"ename":109,"cname":"妲己","title":"魅力之狐","pay_type":11,"new_type":0,"hero_type":2,"skin_name":"魅惑之狐|女仆咖啡|魅力维加斯|仙境爱丽丝|少女阿狸|热情桑巴"},{"ename":110,"cname":"嬴政","title":"王者独尊","new_type":0,"hero_type":2,"skin_name":"王者独尊|摇滚巨星|暗夜贵公子|优雅恋人"},{"ename":111,"cname":"孙尚香","title":"千金重弩","new_type":0,"hero_type":5,"skin_name":"千金重弩|火炮千金|水果甜心|蔷薇恋人|杀手不太冷|末日机甲|沉稳之力"},{"ename":112,"cname":"鲁班七号","title":"机关造物","pay_type":11,"new_type":0,"hero_type":5,"skin_name":"机关造物|木偶奇遇记|福禄兄弟|电玩小子|星空梦想"},{"ename":113,"cname":"庄周","title":"逍遥梦幻","new_type":0,"hero_type":6,"hero_type2":3,"skin_name":"逍遥幻梦|鲤鱼之梦|蜃楼王|云端筑梦师"},{"ename":114,"cname":"刘禅","title":"暴走机关","new_type":0,"hero_type":3,"skin_name":"暴走机关|英喵野望|绅士熊喵"},{"ename":115,"cname":"高渐离","title":"叛逆吟游","new_type":0,"hero_type":2,"skin_name":"叛逆吟游|金属狂潮|死亡摇滚"},{"ename":116,"cname":"阿轲","title":"信念之刃","new_type":0,"hero_type":4,"skin_name":"信念之刃|爱心护理|暗夜猫娘|致命风华"},{"ename":117,"cname":"钟无艳","title":"野蛮之锤","new_type":0,"hero_type":1,"hero_type2":3,"skin_name":"野蛮之锤|生化警戒|王者之锤|海滩丽影"},{"ename":118,"cname":"孙膑","title":"逆流之时","new_type":0,"hero_type":6,"hero_type2":2,"skin_name":"逆流之时|未来旅行|天使之翼|妖精王"},{"ename":119,"cname":"扁鹊","title":"善恶怪医","new_type":0,"hero_type":2,"hero_type2":6,"skin_name":"善恶怪医|救世之瞳|化身博士|炼金王"},{"ename":120,"cname":"白起","title":"最终兵器","new_type":0,"hero_type":3,"skin_name":"最终兵器|白色死神|狰"},{"ename":121,"cname":"芈月","title":"永恒之月","new_type":0,"hero_type":2,"hero_type2":3,"skin_name":"永恒之月|红桃皇后|大秦宣太后|重明"},{"ename":123,"cname":"吕布","title":"无双之魔","new_type":0,"hero_type":1,"hero_type2":3,"skin_name":"无双之魔|圣诞狂欢|天魔缭乱|末日机甲"},{"ename":124,"cname":"周瑜","title":"铁血都督","new_type":0,"hero_type":2,"skin_name":"铁血都督|海军大将|真爱至上"},{"ename":126,"cname":"夏侯惇","title":"不羁之风","new_type":0,"hero_type":3,"hero_type2":1,"skin_name":"不羁之风|战争骑士|乘风破浪"},{"ename":127,"cname":"甄姬","title":"洛神降临","new_type":0,"hero_type":2,"skin_name":"洛神降临|冰雪圆舞曲|花好人间|游园惊梦"},{"ename":128,"cname":"曹操","title":"鲜血枭雄","new_type":0,"hero_type":1,"skin_name":"鲜血枭雄|超能战警|幽灵船长|死神来了|烛龙"},{"ename":129,"cname":"典韦","title":"狂战士","new_type":0,"hero_type":1,"skin_name":"狂战士|黄金武士|穷奇"},{"ename":130,"cname":"宫本武藏","title":"剑圣","new_type":0,"hero_type":1,"skin_name":"剑圣|鬼剑武藏|未来纪元|万象初新|地狱之眼|霸王丸"},{"ename":131,"cname":"李白","title":"青莲剑仙","new_type":0,"hero_type":4,"hero_type2":1,"skin_name":"青莲剑仙|范海辛|千年之狐|凤求凰"},{"ename":132,"cname":"马可波罗","title":"远游之枪","new_type":0,"hero_type":5,"skin_name":"远游之枪|激情绿茵|逐梦之星"},{"ename":133,"cname":"狄仁杰","title":"断案大师","pay_type":11,"new_type":0,"hero_type":5,"skin_name":"断案大师|锦衣卫|魔术师|超时空战士|阴阳师"},{"ename":134,"cname":"达摩","title":"拳僧","new_type":0,"hero_type":1,"hero_type2":3,"skin_name":"拳僧|大发明家|拳王"},{"ename":135,"cname":"项羽","title":"霸王","new_type":0,"hero_type":3,"skin_name":"霸王|帝国元帅|苍穹之光|海滩派对|职棒王牌|霸王别姬"},{"ename":136,"cname":"武则天","title":"女帝","new_type":0,"hero_type":2,"skin_name":"女帝|东方不败|海洋之心"},{"ename":139,"cname":"老夫子","title":"万古长明","new_type":0,"hero_type":1,"skin_name":"万古长明|潮流仙人|圣诞老人|功夫老勺"},{"ename":140,"cname":"关羽","title":"一骑当千","new_type":0,"hero_type":1,"hero_type2":3,"skin_name":"一骑当千|天启骑士|冰锋战神|龙腾万里"},{"ename":141,"cname":"貂蝉","title":"绝世舞姬","new_type":0,"hero_type":2,"hero_type2":4,"skin_name":"绝世舞姬|异域舞娘|圣诞恋歌|逐梦之音|仲夏夜之梦"},{"ename":142,"cname":"安琪拉","title":"暗夜萝莉","new_type":0,"hero_type":2,"skin_name":"暗夜萝莉|玩偶对对碰|魔法小厨娘|心灵骇客"},{"ename":144,"cname":"程咬金","title":"热烈之斧","new_type":0,"hero_type":3,"hero_type2":1,"skin_name":"热烈之斧|爱与正义|星际陆战队|华尔街大亨"},{"ename":146,"cname":"露娜","title":"月光之女","new_type":0,"hero_type":1,"hero_type2":2,"skin_name":"月光之女|哥特玫瑰|绯红之刃|紫霞仙子"},{"ename":148,"cname":"姜子牙","title":"太古魔导","new_type":0,"hero_type":2,"hero_type2":6,"skin_name":"太古魔导|时尚教父"},{"ename":149,"cname":"刘邦","title":"双面君主","new_type":0,"hero_type":3,"hero_type2":6,"skin_name":"双面君主|圣殿之光|德古拉伯爵"},{"ename":150,"cname":"韩信","title":"国士无双","new_type":0,"hero_type":4,"hero_type2":1,"skin_name":"国士无双|街头霸王|教廷特使|白龙吟|逐梦之影"},{"ename":152,"cname":"王昭君","title":"冰雪之华","pay_type":10,"new_type":0,"hero_type":2,"skin_name":"冰雪之华|精灵公主|偶像歌手|凤凰于飞|幻想奇妙夜"},{"ename":153,"cname":"兰陵王","title":"暗影刀锋","new_type":0,"hero_type":4,"skin_name":"暗影刀锋|隐刃|暗隐猎兽者"},{"ename":154,"cname":"花木兰","title":"传说之刃","new_type":0,"hero_type":1,"hero_type2":4,"skin_name":"传说之刃|剑舞者|兔女郎|水晶猎龙者|青春决赛季"},{"ename":156,"cname":"张良","title":"言灵之书","new_type":0,"hero_type":2,"skin_name":"言灵之书|天堂福音|一千零一夜"},{"ename":157,"cname":"不知火舞","title":"明媚烈焰","new_type":0,"hero_type":2,"hero_type2":4,"skin_name":"明媚烈焰"},{"ename":162,"cname":"娜可露露","title":"鹰之守护","new_type":0,"hero_type":4,"skin_name":"鹰之守护"},{"ename":163,"cname":"橘右京","title":"神梦一刀","new_type":0,"hero_type":4,"hero_type2":1,"skin_name":"神梦一刀"},{"ename":166,"cname":"亚瑟","title":"圣骑之力","pay_type":11,"new_type":0,"hero_type":1,"hero_type2":3,"skin_name":"圣骑之力|死亡骑士|狮心王|心灵战警"},{"ename":167,"cname":"孙悟空","title":"齐天大圣","new_type":0,"hero_type":1,"hero_type2":4,"skin_name":"齐天大圣|地狱火|西部大镖客|美猴王|至尊宝"},{"ename":168,"cname":"牛魔","title":"精英酋长","pay_type":10,"new_type":0,"hero_type":3,"hero_type2":6,"skin_name":"精英酋长|西部大镖客|制霸全明星"},{"ename":169,"cname":"后羿","title":"半神之弓","new_type":0,"hero_type":5,"skin_name":"半神之弓|精灵王|阿尔法小队|辉光之辰"},{"ename":170,"cname":"刘备","title":"仁德义枪","new_type":0,"hero_type":1,"skin_name":"仁德义枪|万事如意|纽约教父|汉昭烈帝"},{"ename":171,"cname":"张飞","title":"禁血狂兽","new_type":0,"hero_type":3,"hero_type2":6,"skin_name":"禁血狂兽|五福同心|乱世虎臣"},{"ename":173,"cname":"李元芳","title":"王都密探","new_type":0,"hero_type":5,"skin_name":"王都密探|特种部队|黑猫爱糖果"},{"ename":174,"cname":"虞姬","title":"森之风灵","pay_type":10,"new_type":0,"hero_type":5,"skin_name":"森之风灵|加勒比小姐|霸王别姬|凯尔特女王"},{"ename":175,"cname":"钟馗","title":"虚灵城判","new_type":0,"hero_type":2,"hero_type2":1,"skin_name":"虚灵城判|地府判官"},{"ename":177,"cname":"成吉思汗","title":"苍狼末裔","new_type":0,"hero_type":5,"skin_name":"苍狼末裔|维京掠夺者"},{"ename":178,"cname":"杨戬","title":"根源之目","new_type":0,"hero_type":1,"skin_name":"根源之目|埃及法老|永曜之星"},{"ename":183,"cname":"雅典娜","title":"圣域余晖","new_type":0,"hero_type":1,"skin_name":"圣域余晖|战争女神|冰冠公主|神奇女侠"},{"ename":184,"cname":"蔡文姬","title":"天籁弦音","new_type":0,"hero_type":6,"skin_name":"天籁弦音|蔷薇王座|舞动绿茵"},{"ename":186,"cname":"太乙真人","title":"炼金大师","new_type":0,"hero_type":6,"hero_type2":3,"skin_name":"炼金大师|圆桌骑士|饕餮"},{"ename":180,"cname":"哪吒","title":"桀骜炎枪","pay_type":10,"new_type":0,"hero_type":1,"skin_name":"桀骜炎枪|三太子|逐梦之翼"},{"ename":190,"cname":"诸葛亮","title":"绝代智谋","new_type":0,"hero_type":2,"skin_name":"绝代智谋|星航指挥官|黄金分割率|武陵仙君"},{"ename":192,"cname":"黄忠","title":"燃魂重炮","new_type":0,"hero_type":5,"skin_name":"燃魂重炮|芝加哥教父"},{"ename":191,"cname":"大乔","title":"沧海之曜","new_type":0,"hero_type":6,"skin_name":"沧海之曜|伊势巫女"},{"ename":187,"cname":"东皇太一","title":"噬灭日蚀","new_type":0,"hero_type":3,"skin_name":"噬灭日蚀|东海龙王"},{"ename":182,"cname":"干将莫邪","title":"淬命双剑","new_type":0,"hero_type":2,"skin_name":"淬命双剑|第七人偶"},{"ename":189,"cname":"鬼谷子","title":"万物有灵","new_type":0,"hero_type":6,"skin_name":"万物有灵|阿摩司公爵"},{"ename":193,"cname":"铠","title":"破灭刃锋","new_type":0,"hero_type":1,"hero_type2":3,"skin_name":"破灭刃锋|龙域领主|曙光守护者"},{"ename":196,"cname":"百里守约","title":"静谧之眼","new_type":0,"hero_type":5,"hero_type2":4,"skin_name":"静谧之眼|绝影神枪|特工魅影"},{"ename":195,"cname":"百里玄策","title":"嚣狂之镰","new_type":0,"hero_type":4,"skin_name":"嚣狂之镰|威尼斯狂欢"},{"ename":194,"cname":"苏烈","title":"不屈铁壁","new_type":0,"hero_type":3,"hero_type2":1,"skin_name":"不屈铁壁|爱与和平"},{"ename":198,"cname":"梦奇","title":"入梦之灵","new_type":0,"hero_type":3,"hero_type2":2,"skin_name":"入梦之灵|美梦成真"},{"ename":179,"cname":"女娲","title":"至高创世","pay_type":10,"new_type":0,"hero_type":2,"skin_name":"至高创世|尼罗河女神"},{"ename":501,"cname":"明世隐","title":"灵魂劫卜","new_type":0,"hero_type":6,"skin_name":"灵魂劫卜|占星术士"},{"ename":199,"cname":"公孙离","title":"幻舞玲珑","new_type":0,"hero_type":5,"skin_name":"幻舞玲珑|花间舞"},{"ename":176,"cname":"杨玉环","title":"霓裳风华","new_type":0,"hero_type":2,"hero_type2":6,"skin_name":"风华霓裳|霓裳曲"},{"ename":502,"cname":"裴擒虎","title":"六合虎拳","new_type":0,"hero_type":4,"hero_type2":1,"skin_name":"六合虎拳|街头霸王|梅西"},{"ename":197,"cname":"弈星","title":"天元之弈","new_type":0,"hero_type":2,"skin_name":"天元之弈|踏雪寻梅"},{"ename":503,"cname":"狂铁","title":"战车意志","pay_type":10,"new_type":0,"hero_type":1,"skin_name":"战车意志|命运角斗场"},{"ename":504,"cname":"米莱狄","title":"筑城者","new_type":0,"hero_type":2,"skin_name":"筑城者|精准探案法"},{"ename":125,"cname":"元歌","title":"无间傀儡","new_type":1,"hero_type":4,"skin_name":"无间傀儡|午夜歌剧院"}]
count = 0
for hero in str1:
    count +=1
    f.write('{}.英雄:{},皮肤:{}\n'.format(count,hero['cname'],hero['skin_name']))
f.close()