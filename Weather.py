# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from bs4 import BeautifulSoup
import pymongo
client=pymongo.MongoClient('127.0.0.1',27017)
ceshi=client['ceshi']
item=ceshi['item']
beijing=["北京","海淀","朝阳","顺义","怀柔","通州","昌平","延庆","丰台","石景山","大兴","房山","密云","门头沟","平谷","八达岭","佛爷顶","汤河口","密云上甸子","斋堂","霞云岭"]
shanghai=["上海","闵行","宝山","川沙","嘉定","南汇","金山","青浦","松江","奉贤","崇明","陈家镇","引水船","徐家汇","浦东"]
tianjing=["天津","武清","宝坻","东丽","西青","北辰","宁河","汉沽","静海","津南","塘沽","大港","平台","蓟县"]
chongqin=["重庆","永川","合川","南川","江津","万盛","渝北","北碚","巴南","长寿","黔江","万州天城","万州龙宝","涪陵","开县","城口","云阳","巫溪","奉节","巫山","潼南","垫江","梁平","忠县","石柱","大足","荣昌","铜梁","璧山","丰都","武隆","彭水","綦江","酉阳","金佛山","秀山","沙坪坝"]
heilongjiang=["哈尔滨","双城","呼兰","阿城","宾县","依兰","巴彦","通河","方正","延寿","尚志","五常","木兰","齐齐哈尔","讷河","龙江","甘南","富裕","依安","拜泉","克山","克东","泰来","牡丹江","海林","穆棱","林口","绥芬河","宁安","东宁","佳木斯","汤原","抚远","桦川","桦南","同江","富锦","绥化","肇东","安达","海伦","明水","望奎","兰西","青冈","庆安","绥棱","黑河","嫩江","孙吴","逊克","五大连池","北安","大兴安岭","塔河","漠河","呼玛","呼中","新林","阿木尔","加格达奇","伊春","乌伊岭","五营","铁力","嘉荫","大庆","林甸","肇州","肇源","杜蒙","七台河","勃利","鸡西","虎林","密山","鸡东","鹤岗","绥滨","萝北","双鸭山","集贤","宝清","饶河"]
jingling=["长春","农安","德惠","九台","榆树","双阳","吉林","舒兰","永吉","蛟河","磐石","桦甸","烟筒山","延吉","敦化","安图","汪清","和龙","天池","龙井","珲春","图们","松江","罗子沟","延边","四平","双辽","梨树","公主岭","伊通","孤家子","通化","梅河口","柳河","辉南","集安","通化县","白城","洮南","大安","镇赉","通榆","辽源","东丰","松原","乾安","前郭","长岭","扶余","白山","靖宇","临江","东岗","长白","","沈阳","苏家屯","辽中","康平","法库","新民","于洪","新城子","大连","瓦房店","金州","普兰店","旅顺","长海","庄河","皮口","海洋岛","鞍山","台安","岫岩","海城","抚顺","清原","章党","本溪","本溪县","草河口","桓仁","丹东","凤城","宽甸","东港","东沟","锦州","凌海","北宁","义县","黑山","北镇","营口","大石桥","盖州","阜新","彰武","辽阳","辽阳县","灯塔","铁岭","开原","昌图","西丰","朝阳","建平","凌源","喀左","北票","羊山","建平县","盘锦","大洼","盘山","葫芦岛","建昌","绥中","兴城","","呼和浩特","土默特左旗","托克托","和林格尔","清水河","呼和浩特市郊区","武川","包头","白云鄂博","满都拉","土默特右旗","固阳","达尔罕茂明安联合旗","石拐","乌海","集宁","卓资","化德","商都","希拉穆仁","兴和"]
liaoning=["石家庄","","井陉","正定","栾城","行唐","灵寿","","高邑","深泽","赞皇","无极","","平山","元氏","赵县","辛集","藁城","晋洲","新乐","保定","满城","阜平","徐水","唐县","高阳","容城","紫荆关","涞源","望都","安新","易县","涞水","曲阳","蠡县","顺平","雄县","涿州","定州","安国","高碑店","张家口","宣化","张北","康保","沽源","尚义","蔚县","阳原","怀安","万全","怀来","涿鹿","赤城","崇礼","承德","承德县","兴隆","平泉","滦平","隆化","丰宁","宽城","围场","塞罕坎","唐山","丰南","丰润","滦县","滦南","乐亭","迁西","玉田","唐海","遵化","迁安","廊坊","固安","永清","香河","大城","文安","大厂","霸州","三河","沧州","青县","东光","海兴","盐山","肃宁","南皮","吴桥","献县","孟村","泊头","任丘","黄骅","河间","曹妃甸","衡水","枣强","武邑","武强","饶阳","安平","故城","景县","阜城","冀州","深州","邢台","临城","邢台县浆水","内邱","柏乡","隆尧","南和","宁晋","巨鹿","新河","广宗","平乡","威县","清河","临西","南宫","沙河","任县","邯郸","峰峰","临漳","成安","大名","涉县","磁县","肥乡","永年"]
neimenggu=["太原","清徐","阳曲","娄烦","太原古交区","太原北郊","太原南郊","大同","阳高","大同县","天镇","广灵","灵邱","浑源","左云","阳泉","盂县","平定","晋中","榆次","榆社","左权","和顺","昔阳","寿阳","太谷","祁县","平遥","灵石","介休","长治","黎城","屯留","潞城","襄垣","平顺","武乡","沁县","长子","沁源","壶关","晋城","沁水","阳城","陵川","高平","临汾","曲沃","永和","隰县","大宁","吉县","襄汾","蒲县","汾西","洪洞","霍州","乡宁","翼城","侯马","浮山","安泽","古县","运城","临猗","稷山","万荣","河津","新绛","绛县","闻喜","垣曲","永济","芮城","夏县","平陆","朔州","平鲁","山阴","右玉","应县","怀仁","忻州","定襄","五台县豆村","河曲","偏关","神池","宁武","代县","繁峙","五台山","凉城","察哈尔右翼前旗","察哈尔右翼中旗","察哈尔右翼后旗","四子王旗","丰镇","通辽","舍伯吐","科尔沁左翼中旗","科尔沁左翼后旗","青龙山","开鲁","库伦旗","奈曼旗","扎鲁特旗","高力板","巴雅尔吐胡硕","通辽钱家店","赤峰","赤峰郊区站","阿鲁科尔沁旗","浩尔吐","巴林左旗","巴林右旗","林西","克什克腾旗","翁牛特旗","岗子","喀喇沁旗","八里罕","宁城","敖汉旗","宝过图","鄂尔多斯","达拉特旗","准格尔旗","鄂托克前旗","河南","伊克乌素","鄂托克旗","杭锦旗","乌审旗","伊金霍洛旗","乌审召","东胜","临河","五原","磴口","乌拉特前旗","大佘太","乌拉特中旗","乌拉特后旗","海力素","那仁宝力格","杭锦后旗","巴盟农试站","锡林浩特","朝克乌拉","二连浩特","阿巴嘎旗","伊和郭勒","苏尼特左旗","苏尼特右旗","朱日和","东乌珠穆沁旗","西乌珠穆沁旗","太仆寺旗","镶黄旗","正镶白旗","正兰旗","多伦","博克图","乌拉盖","白日乌拉","那日图","呼伦贝尔","海拉尔","小二沟","阿荣旗","莫力达瓦旗","鄂伦春旗","鄂温克旗","陈巴尔虎旗","新巴尔虎左旗","新巴尔虎右旗"]
hebei=["西安","长安","临潼","蓝田","周至","户县","高陵","杨凌","咸阳","三原","礼泉","永寿","淳化","泾阳","武功","乾县","彬县","长武","旬邑","兴平","延安","延长","延川","子长","宜川","富县","志丹","安塞","甘泉","洛川","黄陵","黄龙","吴起","榆林","府谷","神木","佳县","定边","靖边","横山","米脂","子洲","绥德","吴堡","清涧","渭南","华县","潼关","大荔","白水","富平","蒲城","澄城","合阳","韩城","华阴","华山","商洛","洛南","柞水","镇安","丹凤","商南","山阳","安康","紫阳","石泉","汉阴","旬阳","岚皋","平利","白河","镇坪","宁陕","汉中","略阳","勉县","留坝","洋县","城固","西乡","佛坪","宁强","南郑","镇巴","宝鸡","宝鸡县","千阳","麟游","岐山","凤翔","扶风","眉县","太白","凤县","陇县","铜川","耀县","宜君"]
shanxi=["西安","长安","临潼","蓝田","周至","户县","高陵","杨凌","咸阳","三原","礼泉","永寿","淳化","泾阳","武功","乾县","彬县","长武","旬邑","兴平","延安","延长","延川","子长","宜川","富县","志丹","安塞","甘泉","洛川","黄陵","黄龙","吴起","榆林","府谷","神木","佳县","定边","靖边","横山","米脂","子洲","绥德","吴堡","清涧","渭南","华县","潼关","大荔","白水","富平","蒲城","澄城","合阳","韩城","华阴","华山","商洛","洛南","柞水","镇安","丹凤","商南","山阳","安康","紫阳","石泉","汉阴","旬阳","岚皋","平利","白河","镇坪","宁陕","汉中","略阳","勉县","留坝","洋县","城固","西乡","佛坪","宁强","南郑","镇巴","宝鸡","宝鸡县","千阳","麟游","岐山","凤翔","扶风","眉县","太白","凤县","陇县","铜川","耀县","宜君"]
shandong=["济南","长清","商河","章丘","平阴","济阳","青岛","崂山","潮连岛","即墨","胶州","胶南","莱西","平度","淄博","淄川","博山","高青","周村","沂源","桓台","临淄","德州","武城","临邑","陵县","齐河","乐陵","庆云","平原","宁津","夏津","禹城","烟台","莱州","长岛","蓬莱","龙口","招远","栖霞","福山","牟平","莱阳","海阳","千里岩","潍坊","青州","寿光","临朐","昌乐","昌邑","安丘","高密","诸城","济宁","嘉祥","微山","鱼台","兖州","金乡","汶上","泗水","梁山","曲阜","邹城","泰安","新泰","泰山","肥城","东平","宁阳","临沂","莒南","沂南","苍山","临沭","郯城","蒙阴","平邑","费县","沂水","马站","菏泽","鄄城","郓城","东明","定陶","巨野","曹县","成武","单县","滨州","博兴","无棣","阳信","惠民","沾化","邹平","东营","河口","垦利","利津","广饶","威海","文登","荣成","乳山","成山头","石岛","枣庄","薛城","峄城","台儿庄","滕州","日照","五莲","莒县","莱芜","聊城","冠县","阳谷","高唐","茌平","东阿","临清","朝城","莘县"]
xinjiang=["乌鲁木齐","蔡家湖","小渠子","巴仑台","达坂城","十三间房气象站","天山大西沟","乌鲁木齐牧试站","天池","白杨沟","克拉玛依","石河子","炮台","莫索湾","乌兰乌苏","昌吉","呼图壁","米泉","阜康","吉木萨尔","奇台","玛纳斯","木垒","北塔山","吐鲁番","托克逊","吐鲁番东坎","鄯善","红柳河","库尔勒","轮台","尉犁","若羌","且末","和静","焉耆","和硕","库米什","巴音布鲁克","铁干里克","博湖","塔中","阿拉尔","阿克苏","乌什","温宿","拜城","新和","沙雅","库车","柯坪","阿瓦提","喀什","英吉沙","塔什库尔干","麦盖提","莎车","叶城","泽普","巴楚","岳普湖","伽师","伊宁","察布查尔","尼勒克","伊宁县","巩留","新源","昭苏","特克斯","霍城","霍尔果斯","塔城","裕民","额敏","和布克赛尔","托里","乌苏","沙湾","和丰","哈密","沁城","巴里坤","伊吾","淖毛湖","和田","皮山","策勒","墨玉","洛浦","民丰","于田","阿勒泰","哈巴河","一八五团","黑山头","吉木乃","布尔津","福海","富蕴","青河","安德河","阿图什","乌恰","阿克陶","阿合奇","吐尔尕特","博乐","温泉","精河","阿拉山口"]
xizhang=["拉萨","当雄","尼木","墨竹贡卡","日喀则","拉孜","南木林","聂拉木","定日","江孜","帕里","山南","贡嘎","琼结","加查","浪卡子","错那","隆子","泽当","林芝","波密","米林","察隅","昌都","丁青","类乌齐","洛隆","左贡","芒康","八宿","那曲","嘉黎","班戈","安多","索县","比如","阿里","改则","申扎","狮泉河","普兰"]
qinghai=["西宁","大通","湟源","湟中","铁卜加","铁卜加寺","中心站","海东","乐都","民和","互助","化隆","循化","冷湖","平安","黄南","尖扎","泽库","河南","海南","江西沟","贵德","河卡","兴海","贵南","同德","共和","果洛","班玛","甘德","达日","久治","玛多","清水河","玛沁","玉树","托托河","治多","杂多","囊谦","曲麻莱","海西","格尔木","察尔汉","野牛沟","五道梁","小灶火","天峻","乌兰","都兰","诺木洪","茫崖","大柴旦","茶卡","香日德","德令哈","海北","门源","祁连","海晏","托勒","刚察"]
ganshu=["兰州","皋兰","永登","榆中","定西","通渭","陇西","渭源","临洮","漳县","岷县","安定","平凉","泾川","灵台","崇信","华亭","庄浪","静宁","崆峒","庆阳","西峰","环县","华池","合水","正宁","宁县","镇原","庆城","武威","民勤","古浪","乌鞘岭","天祝","金昌","永昌","张掖","肃南","民乐","临泽","高台","山丹","酒泉","鼎新","金塔","马鬃山","瓜州","肃北","玉门镇","敦煌","天水","北道区","清水","秦安","甘谷","武山","张家川","麦积","武都","成县","文县","宕昌","康县","西和","礼县","徽县","两当","临夏","康乐","永靖","广河","和政","东乡","合作","临潭","卓尼","舟曲","迭部","玛曲","碌曲","夏河","白银","靖远","会宁","华家岭","景泰"]
ningxia=["银川","永宁","灵武","贺兰","石嘴山","惠农","平罗","陶乐","石炭井","大武口","吴忠","同心","盐池","韦州","麻黄山","青铜峡","固原","西吉","隆德","泾源","六盘山","彭阳","中卫","中宁","兴仁堡","海原"]
henan=["郑州","巩义","荥阳","登封","新密","新郑","中牟","郑州农试站","安阳","汤阴","滑县","内黄","林州","新乡","获嘉","原阳","辉县","卫辉","延津","封丘","长垣","许昌","鄢陵","襄城","长葛","禹州","平顶山","郏县","宝丰","汝州","叶县","舞钢","鲁山","信阳","息县","罗山","光山","新县","淮滨","潢川","固始","商城","鸡公山","信阳地区农试站","南阳","南召","方城","社旗","西峡","内乡","镇平","淅川","新野","唐河","邓州","桐柏","开封","杞县","尉氏","通许","兰考","洛阳","新安","孟津","宜阳","洛宁","伊川","嵩县","偃师","栾川","汝阳","商丘","睢阳区","睢县","民权","虞城","柘城","宁陵","夏邑","永城","焦作","修武","武陟","沁阳","博爱","温县","孟州","鹤壁","浚县","淇县","濮阳","台前","南乐","清丰","范县","周口","扶沟","太康","淮阳","西华","商水","项城","郸城","鹿邑","沈丘","黄泛区","漯河","临颍","舞阳","驻马店","西平","遂平","上蔡","汝南","泌阳","平舆","新蔡","确山","正阳","三门峡","灵宝","渑池","卢氏","济源"]
jiangshu=["南京","溧水","高淳","江宁","六合","江浦","浦口","无锡","江阴","宜兴","镇江","丹阳","扬中","句容","丹徒","苏州","常熟","张家港","昆山","吴县东山","吴县","吴江","太仓","南通","海安","如皋","如东","吕泗","吕泗渔场","启东","海门","通州","扬州","宝应","仪征","高邮","江都","邗江","盐城","响水","滨海","阜宁","射阳","建湖","东台","大丰","盐都","徐州","徐州农试站","丰县","沛县","邳州","睢宁","新沂","淮安","金湖","盱眙","洪泽","涟水","淮阴县","淮阴","楚州","连云港","东海","赣榆","灌云","灌南","西连岛","燕尾港","常州","溧阳","金坛","泰州","兴化","泰兴","姜堰","靖江","宿迁","沭阳","泗阳","泗洪"]
hubei=["武汉","蔡甸","黄陂","新洲","江夏","襄樊","襄阳","保康","南漳","宜城","老河口","谷城","枣阳","鄂州","孝感","安陆","云梦","大悟","应城","汉川","黄冈","红安","麻城","罗田","英山","浠水","蕲春","黄梅","武穴","黄石","大冶","阳新","咸宁","赤壁","嘉鱼","崇阳","通城","通山","荆州","江陵","公安","石首","监利","洪湖","松滋","宜昌","远安","秭归","兴山","宜昌县","五峰","当阳","长阳","宜都","枝江","三峡","夷陵","恩施","利川","建始","咸丰","宣恩","鹤峰","来凤","巴东","绿葱坡","十堰","竹溪","郧西","郧县","竹山","房县","丹江口","神农架","随州","广水","荆门","钟祥","京山","天门","仙桃","潜江"]
zhejiang=["杭州","萧山","桐庐","淳安","建德","余杭","临安","富阳","湖州","长兴","安吉","德清","嘉兴","嘉善","海宁","桐乡","平湖","海盐","宁波","慈溪","余姚","奉化","象山","石浦","宁海","鄞县","北仑","鄞州","镇海","绍兴","诸暨","上虞","新昌","嵊州","台州","括苍山","玉环","三门","天台","仙居","温岭","大陈","洪家","温州","泰顺","文成","平阳","瑞安","洞头","乐清","永嘉","苍南","丽水","遂昌","龙泉","缙云","青田","云和","庆元","金华","浦江","兰溪","义乌","东阳","武义","永康","磐安","衢州","常山","开化","龙游","江山","舟山","嵊泗","嵊山","岱山","普陀","定海"]
anhui=["合肥","长丰","肥东","肥西","蚌埠","怀远","固镇","五河","芜湖","繁昌","芜湖县","南陵","淮南","凤台","马鞍山","当涂","安庆","枞阳","太湖","潜山","怀宁","宿松","望江","岳西","桐城","宿州","砀山","灵璧","泗县","萧县","阜阳","阜南","颍上","临泉","界首","太和","亳州","涡阳","利辛","蒙城","黄山站","黄山区","屯溪","祁门","黟县","歙县","休宁","黄山市","滁州","凤阳","明光","定远","全椒","来安","天长","淮北","濉溪","铜陵","宣城","泾县","旌德","宁国","绩溪","广德","郎溪","六安","霍邱","寿县","南溪","金寨","霍山","舒城","巢湖","庐江","无为","含山","和县","池州","东至","青阳","九华山","石台"]
fujian=["福州","闽清","闽侯","罗源","连江","马祖","永泰","平潭","福州郊区","长乐","福清","平潭海峡大桥","厦门","同安","宁德","古田","霞浦","寿宁","周宁","福安","柘荣","福鼎","屏南","莆田","仙游","秀屿港","泉州","安溪","九仙山","永春","德化","南安","崇武","金山","晋江","漳州","长泰","南靖","平和","龙海","漳浦","诏安","东山","云霄","华安","龙岩","长汀","连城","武平","上杭","永定","漳平","三明","宁化","清流","泰宁","将乐","建宁","明溪","沙县","尤溪","永安","大田","南平","顺昌","光泽","邵武","武夷山","浦城","建阳","松溪","政和","建瓯"]
jiangxi=["南昌","新建","南昌县","安义","进贤","莲塘","九江","瑞昌","庐山","武宁","德安","永修","湖口","彭泽","星子","都昌","棠荫","修水","上饶","鄱阳","婺源","康山","余干","万年","德兴","上饶县","弋阳","横峰","铅山","玉山","广丰","波阳","抚州","广昌","乐安","崇仁","金溪","资溪","宜黄","南城","南丰","黎川","东乡","宜春","铜鼓","宜丰","万载","上高","靖安","奉新","高安","樟树","丰城","吉安","吉安县","吉水","新干","峡江","永丰","永新","井冈山","万安","遂川","泰和","安福","宁冈","赣州","崇义","上犹","南康","大余","信丰","宁都","石城","瑞金","于都","会昌","安远","全南","龙南","定南","寻乌","兴国","景德镇","乐平","萍乡","莲花","新余","分宜","鹰潭","余江","贵溪"]
hunan=["长沙","宁乡","浏阳","马坡岭","湘潭","韶山","湘乡","株洲","攸县","醴陵","株洲县","茶陵","炎陵","衡阳","衡山","衡东","祁东","衡阳县","常宁","衡南","耒阳","南岳","郴州","桂阳","嘉禾","宜章","临武","桥口","资兴","汝城","安仁","永兴","桂东","常德","安乡","桃源","汉寿","澧县","临澧","石门","益阳","赫山区","南县","桃江","安化","沅江","娄底","双峰","冷水江","冷水滩","新化","涟源","邵阳","隆回","洞口","新邵","邵东","绥宁","新宁","武冈","城步","邵阳县","岳阳","华容","湘阴","汨罗","平江","临湘","张家界","桑植","慈利","怀化","鹤城区","沅陵","辰溪","靖州","会同","通道","麻阳","新晃","芷江","溆浦","黔阳","洪江","永州","祁阳","东安","双牌","道县","宁远","江永","蓝山","新田","江华","吉首","保靖","永顺","古丈","凤凰","泸溪","龙山","花垣"]
guizhou=["贵阳","白云","花溪","乌当","息烽","开阳","修文","清镇","遵义","遵义县","仁怀","绥阳","湄潭","凤冈","桐梓","赤水","习水","道真","正安","务川","余庆","汇川","安顺","普定","镇宁","平坝","紫云","关岭","都匀","贵定","瓮安","长顺","福泉","惠水","龙里","罗甸","平塘","独山","三都","荔波","凯里","岑巩","施秉","镇远","黄平","黄平旧洲","麻江","丹寨","三穗","台江","剑河","雷山","黎平","天柱","锦屏","榕江","从江","炉山","铜仁","江口","玉屏","万山","思南","塘头","印江","石阡","沿河","德江","松桃","毕节","赫章","金沙","威宁","大方","纳雍","织金","六盘水","六枝","水城","盘县","黔西","晴隆","兴仁","贞丰","望谟","兴义","安龙","册亨","普安"]
sichuan=["成都","龙泉驿","新都","温江","金堂","双流","郫县","大邑","蒲江","新津","都江堰","彭州","邛崃","崇州","崇庆","彭县","攀枝花","仁和","米易","盐边","自贡","富顺","荣县","绵阳","三台","盐亭","安县","梓潼","北川","平武","江油","南充","南部","营山","蓬安","仪陇","西充","阆中","达州","宣汉","开江","大竹","渠县","万源","达川","遂宁","蓬溪","射洪","广安","岳池","武胜","邻水","华蓥山","巴中","通江","南江","平昌","泸州","泸县","合江","叙永","古蔺","纳溪","宜宾","宜宾农试站","宜宾县","南溪","江安","长宁","高县","珙县","筠连","兴文","屏山","内江","东兴","威远","资中","隆昌","资阳","安岳","乐至","简阳","乐山","犍为","井研","夹江","沐川","峨边","马边","峨眉","峨眉山","眉山","仁寿","彭山","洪雅","丹棱","青神","凉山","木里","盐源","德昌","会理","会东","宁南","普格","西昌","金阳","昭觉","喜德","冕宁","越西","甘洛","雷波","美姑","布拖","雅安","名山","荣经","汉源","石棉","天全","芦山","宝兴","甘孜","康定","泸定","丹巴","九龙","雅江","道孚","炉霍","新龙","德格","白玉","石渠","色达","理塘","巴塘","乡城","稻城","得荣","阿坝","汶川","理县","茂县","松潘","九寨沟","金川","小金","黑水","马尔康","壤塘","若尔盖","红原","南坪","德阳","中江","广汉","什邡","绵竹","罗江","广元","旺苍","青川","剑阁","苍溪"]
guangdong=["广州","番禺","从化","增城","花都","天河","韶关","乳源","始兴","翁源","乐昌","仁化","南雄","新丰","曲江","惠州","博罗","惠阳","惠东","龙门","梅州","兴宁","蕉岭","大埔","丰顺","平远","五华","梅县","汕头","潮阳","澄海","南澳","云澳","南澎岛","深圳","珠海","斗门","黄茅洲","佛山","顺德","三水","南海","肇庆","广宁","四会","德庆","怀集","封开","高要","湛江","吴川","雷州","徐闻","廉江","硇洲","遂溪","江门","开平","新会","恩平","台山","上川岛","鹤山","河源","紫金","连平","和平","龙川","清远","连南","连州","连山","阳山","佛冈","英德","云浮","罗定","新兴","郁南","潮州","饶平","东莞","中山","阳江","阳春","揭阳","揭西","普宁","惠来","茂名","高州","化州","电白","信宜","汕尾","海丰","陆丰","遮浪","东沙岛"]
yunnan=["昆明","昆明农试站","东川","寻甸","晋宁","宜良","石林","呈贡","富民","嵩明","禄劝","安宁","太华山","河口","大理","云龙","漾鼻","永平","宾川","弥渡","祥云","魏山","剑川","洱源","鹤庆","南涧","红河","石屏","建水","弥勒","元阳","绿春","开远","个旧","蒙自","屏边","泸西","金平","曲靖","沾益","陆良","富源","马龙","师宗","罗平","会泽","宣威","保山","富宁","龙陵","施甸","昌宁","腾冲","文山","西畴","马关","麻栗坡","砚山","邱北","广南","玉溪","澄江","江川","通海","华宁","新平","易门","峨山","元江","楚雄","大姚","元谋","姚安","牟定","南华","武定","禄丰","双柏","永仁","普洱","景谷","景东","澜沧","普洱","墨江","江城","孟连","西盟","镇源","镇沅","宁洱","昭通","鲁甸","彝良","镇雄","威信","巧家","绥江","永善","盐津","大关","临沧","沧源","耿马","双江","凤庆","永德","云县","镇康","怒江","福贡","兰坪","泸水","六库","贡山","香格里拉","德钦","维西","中甸","丽江","永胜","华坪","宁蒗","德宏","潞江坝","陇川","盈江","畹町镇","瑞丽","梁河","潞西","景洪","大勐龙","勐海","景洪电站","勐腊"]
guangxi=["南宁","南宁城区","邕宁","横县","隆安","马山","上林","武鸣","宾阳","硕龙","崇左","天等","龙州","凭祥","大新","扶绥","宁明","海渊","柳州","柳城","沙塘","鹿寨","柳江","融安","融水","三江","来宾","忻城","金秀","象州","武宣","桂林","桂林农试站","龙胜","永福","临桂","兴安","灵川","全州","灌阳","阳朔","恭城","平乐","荔浦","资源","梧州","藤县","太平","苍梧","蒙山","岑溪","贺州","昭平","富川","钟山","信都","贵港","桂平","平南","玉林","博白","北流","容县","陆川","百色","那坡","田阳","德保","靖西","田东","平果","隆林","西林","乐业","凌云","田林","钦州","浦北","灵山","河池","天峨","东兰","巴马","环江","罗城","宜州","凤山","南丹","都安","北海","合浦","涠洲岛","防城港","上思","东兴","板栏","防城"]
hainan=["海口","琼山","三亚","东方","临高","澄迈","儋州","昌江","白沙","琼中","定安","屯昌","琼海","文昌","清兰","保亭","万宁","陵水","西沙","珊瑚岛","永署礁","南沙岛","乐东","五指山","通什"]
xianggang=["香港","九龙","新界","中环","铜锣湾"]
aomeng=["澳门"]
taiwan=["台北县","台北市","高雄","东港","大武","恒春","兰屿","台南","台中","桃园","新竹县","新竹市","公馆","宜兰","马公","东吉屿","嘉义","阿里山","玉山","新港"]
class Ui_Form(object):
	def setupUi(self,Form):
		Form.setObjectName("Form")
		Form.resize(450, 347)
		self.data = []
		self.data1=[]
		self.get_id1()
		self.get_id2()
		self.get_id3()
		self.get_id4()
		self.get_name()
		self.groupBox = QtWidgets.QGroupBox(Form)
		self.groupBox.setGeometry(QtCore.QRect(10, 10, 431, 251))
		self.groupBox.setObjectName("groupBox")
		
		self.weatherComboBox = QtWidgets.QComboBox(self.groupBox)
		self.weatherComboBox.setGeometry(QtCore.QRect(80, 30, 100, 21))
		self.weatherComboBox1 = QtWidgets.QComboBox(self.groupBox)
		self.weatherComboBox1.setGeometry(QtCore.QRect(200, 30, 100, 21))
		self.weatherComboBox1.setObjectName("weatherComboBox1")
		self.resultText = QtWidgets.QTextEdit(self.groupBox)
		self.resultText.setFontPointSize(14)
		self.resultText.setGeometry(QtCore.QRect(10, 60, 411, 181))
		self.resultText.setObjectName("resultText")
		
		self.label1=QtWidgets.QLabel(self.groupBox)
		self.label1.setGeometry(QtCore.QRect(300,300,300,300))
		
		self.label = QtWidgets.QLabel(self.groupBox)
		self.label.setGeometry(QtCore.QRect(20, 30, 72, 21))
		self.label.setObjectName("label")
		self.label1.setObjectName("label1")
		self.queryBtn = QtWidgets.QPushButton(Form)
		self.queryBtn.setGeometry(QtCore.QRect(90, 300, 93, 28))
		self.queryBtn.setObjectName("queryBtn")
		self.clearBtn = QtWidgets.QPushButton(Form)
		self.clearBtn.setGeometry(QtCore.QRect(230, 300, 93, 28))
		self.clearBtn.setObjectName("clearBtn")
		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)
	def get_item(self,name):
		for i in range(len(name)):
			self.weatherComboBox1.addItem("")
			self.weatherComboBox1.setItemText(i,name[i])
	def retranslateUi(self, Form):
		privence=["北京","上海","天津","重庆","黑龙江","吉林","辽宁","内蒙古","河北","山西","陕西","山东","新疆","西藏","青海","甘肃","宁夏","河南","江苏","湖北","安徽","福建","江西","湖南","贵州","四川","广东","云南","广西","海南","香港","澳门","台湾"]
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "天气查询"))
		self.groupBox.setTitle(_translate("Form", "查询城市天气"))
		for i in range(len(privence)):
			self.weatherComboBox.addItem("")
			self.weatherComboBox.setItemText(i, _translate("Form", privence[i]))
		self.label.setText(_translate("Form", "省份"))
		self.label1.setText(_translate("Form","版权：139140520@qq.com"))
		self.queryBtn.setText(_translate("Form", "查询"))
		self.clearBtn.setText(_translate("Form", "清空"))
		self.weatherComboBox.currentIndexChanged.connect(self.selection)
		self.weatherComboBox1.currentIndexChanged.connect(self.selection_page)
		self.queryBtn.clicked.connect(self.chaxun)
		self.clearBtn.clicked.connect(self.qingchu)

	def selection(self):
		if self.weatherComboBox.currentText()=="北京":
			self.get_item(beijing)
		elif self.weatherComboBox.currentText() == "上海":
				self.get_item(shanghai)
		elif self.weatherComboBox.currentText() == "天津":
			self.get_item(tianjing)
		elif self.weatherComboBox.currentText() == "重庆":
			self.get_item(chongqin)
		elif self.weatherComboBox.currentText() == "黑龙江":
			self.get_item(heilongjiang)
		elif self.weatherComboBox.currentText() == "吉林":
			self.get_item(jingling)
		elif self.weatherComboBox.currentText() == "辽宁":
				self.get_item(liaoning)
		elif self.weatherComboBox.currentText() == "内蒙古":
				self.get_item(neimenggu)
		elif self.weatherComboBox.currentText() == "河北":
				self.get_item(hebei)
		elif self.weatherComboBox.currentText() == "山西":
				self.get_item(shanxi)
		elif self.weatherComboBox.currentText() == "陕西":
				self.get_item(shanxi)
		elif self.weatherComboBox.currentText() == "山东":
				self.get_item(shandong)
		elif self.weatherComboBox.currentText() == "新疆":
				self.get_item(xinjiang)
		elif self.weatherComboBox.currentText() == "西藏":
				self.get_item(xizhang)
		elif self.weatherComboBox.currentText() == "青海":
			self.get_item(qinghai)
		elif self.weatherComboBox.currentText() == "甘肃":
			self.get_item(ganshu)
		elif self.weatherComboBox.currentText() == "宁夏":
				self.get_item(ningxia)
		elif self.weatherComboBox.currentText() == "河南":
				self.get_item(henan)
		elif self.weatherComboBox.currentText() == "江苏":
				self.get_item(jiangshu)
		elif self.weatherComboBox.currentText() == "湖北":
				self.get_item(hubei)
		elif self.weatherComboBox.currentText() == "浙江":
				self.get_item(zhejiang)
		elif self.weatherComboBox.currentText() == "安徽":
				self.get_item(anhui)
		elif self.weatherComboBox.currentText() == "福建":
				self.get_item(fujian)
		elif self.weatherComboBox.currentText() == "江西":
				self.get_item(jiangxi)
		elif self.weatherComboBox.currentText() == "湖南":
				self.get_item(hunan)
		elif self.weatherComboBox.currentText() == "贵州":
				self.get_item(guizhou)
		elif self.weatherComboBox.currentText() == "四川":
				self.get_item(sichuan)
		elif self.weatherComboBox.currentText() == "广东":
				self.get_item(guangdong)
		elif self.weatherComboBox.currentText() == "云南":
				self.get_item(yunnan)
		elif self.weatherComboBox.currentText() == "广西":
				self.get_item(guangxi)
		elif self.weatherComboBox.currentText() == "海南":
				self.get_item(hainan)
		elif self.weatherComboBox.currentText() == "香港":
				self.get_item(xianggang)
		elif self.weatherComboBox.currentText() == "澳门":
			self.get_item(aomeng)
		elif self.weatherComboBox.currentText() == "台湾":
			self.get_item(taiwan)

	def get_id1(self):
		strat_url = "https://www.cnblogs.com/danyueweb/p/3521973.html"
		re = requests.get(strat_url)
		re.encoding = 'utf-8'
		soup = BeautifulSoup(re.text, 'lxml')
		for i in range(6, 15):
			ids = soup.select('#cnblogs_post_body > p:nth-of-type({})'.format(str(i)))
			for id in ids:
				datas = id.text.split(str(1010))
				for data in datas:
					if data == '':
						pass
					else:
						self.end_id = data.split('=')

						if len(self.end_id[0]) < 5:
							pass
						else:
							self.id1= "1010" + self.end_id[0]
							self.name1=self.end_id[1]
							self.data.append(self.id1)
							self.data1.append(self.name1)


	def get_id2(self):
		strat_url = "https://www.cnblogs.com/danyueweb/p/3521973.html"
		re = requests.get(strat_url)
		re.encoding = 'utf-8'
		soup = BeautifulSoup(re.text, 'lxml')
		for i in range(15, 25):
			ids = soup.select('#cnblogs_post_body > p:nth-of-type({})'.format(str(i)))
			for id in ids:
				datas = id.text.split(str(1011))
				for data in datas:
					if data == '':
						pass
					else:
						self.end_id1 = data.split('=')

						if len(self.end_id1[0]) < 5:
							pass
						else:
							self.id2 = "1011" + self.end_id1[0]
							self.name2=self.end_id1[1]
							self.data.append(self.id2)
							self.data1.append(self.name2)

	def get_id3(self):
		strat_url = "https://www.cnblogs.com/danyueweb/p/3521973.html"
		re = requests.get(strat_url)
		re.encoding = 'utf-8'
		soup = BeautifulSoup(re.text, 'lxml')
		for i in range(25, 35):
			ids = soup.select('#cnblogs_post_body > p:nth-of-type({})'.format(str(i)))
			for id in ids:
				datas = id.text.split(str(1012))
				for data in datas:
					if data == '':
						pass
					else:
						self.end_id2 = data.split('=')
						if len(self.end_id2[0]) < 5:
							pass
						else:
							self.id3 = "1012" + self.end_id2[0]
							self.name3=self.end_id2[1]
							self.data.append(self.id3)
							self.data1.append(self.name3)

	def get_id4(self):
		strat_url = "https://www.cnblogs.com/danyueweb/p/3521973.html"
		re = requests.get(strat_url)
		re.encoding = 'utf-8'

		soup = BeautifulSoup(re.text, 'lxml')
		for i in range(35, 40):
			ids = soup.select('#cnblogs_post_body > p:nth-of-type({})'.format(str(i)))
			for id in ids:
				datas = id.text.split(str(1013))
				for data in datas:
					if data == '':
						pass
					else:
						self.end_id3 = data.split('=')
						if len(self.end_id3[0]) < 5:
							pass
						else:
							self.id4= "1013" + self.end_id3[0]
							self.name4=self.end_id3[1]
							self.data.append(self.id4)
							self.data1.append(self.name4)
	def get_name(self):
		print(len(self.data))
	def selection_page(self):
		for i in range(2582):
			if self.weatherComboBox1.currentText()==self.data1[i]:
				print(self.data[i])
				self.get_url(self.data[i])

	def get_url(self,url):
		header = {
			"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3554.0 Safari/537.36'
		}
		strat_url = "http://www.weather.com.cn/weather1d/{}.shtml".format(str(url))
		re = requests.get(strat_url, headers=header)
		re.encoding = "utf-8"
		soup = BeautifulSoup(re.text, 'lxml')
		didians = soup.select(
			'body > div.con.today.clearfix > div.left.fl > div:nth-child(1) > div.ctop.clearfix > div.crumbs.fl > a:nth-child(3)')
		didians1 = soup.select(
			'body > div.con.today.clearfix > div.left.fl > div:nth-child(1) > div.ctop.clearfix > div.crumbs.fl > a:nth-child(5)')
		sunups = soup.select('#today > div.t > ul > li:nth-of-type(1) > p.sun.sunUp > span')
		sundowns = soup.select('#today > div.t > ul > li:nth-of-type(2) > p.sun.sunDown > span')
		baitians = soup.select('#today > div.t > ul > li:nth-of-type(1) > h1')
		baitiantianqis = soup.select('#today > div.t > ul > li:nth-of-type(1) > p.wea')
		wanshangs = soup.select('#today > div.t > ul > li:nth-of-type(2) > h1')
		wanshangtianqis = soup.select('#today > div.t > ul > li:nth-of-type(2)> p.wea')
		wanshang_temps = soup.select('#today > div.t > ul > li:nth-of-type(2) > p.tem > span')
		fengs = soup.select('.win > span')
		mains = soup.select('#hidden_title')
		hellos = soup.select('p.tem > span:nth-of-type(1)')
		times = soup.select('#fc_24h_internal_update_time')
		if didians == None:
			didians = ["未知"]
		if didians1 == None:
			didians1 = [""]
		for did, didian, sunup, sundown, baitiantianqi, baitian, wanshangtianqi, wanshang, wanshang_temp, feng, main, hello, time in zip(
				didians1,
				didians, sunups, sundowns, baitiantianqis, baitians, wanshangtianqis, wanshangs, wanshang_temps, fengs,
				mains, hellos, times):
			msg1 = "地址：" + didian.get_text() + did.get_text() + "\n"
			msg2 = sunup.get_text() + "\n"
			msg3 = sundown.get_text() + "\n"
			msg4 = baitian.get_text() + " " + baitiantianqi.get_text() + "  温度:" + hello.get_text() + "C°" + "\n"
			msg5 = wanshangtianqi.get_text() + " " + wanshang.get_text() + "  温度:" + wanshang_temp.get_text() + "C°" + "\n"
			msg6 = "大致情况：" + main["value"] + "\n"
			msg7 = "风向：" + feng["title"] + "\n"
			msg8 = "风力：" + feng.get_text() + "\n"
			msg9 = "更新时间:" + time["value"] + "\n"
			self.resultspp = (msg1 + msg2 + msg3 + msg4 + msg5 + msg6 + msg7 + msg8 + msg9)
	def qingchu(self):
	 	self.resultText.clear()
	def chaxun(self):
		self.resultText.setPlainText(self.resultspp)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())