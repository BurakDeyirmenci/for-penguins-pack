from engine import Chapter, Q

create = Chapter("create", "Create", "create:cogwheel", "tech", sub="Dişliler, miller ve dönme gücü", quests=[
    Q("cr_alloy", "create:andesite_alloy*8", sub="Create'in temel malzemesi", shape="hexagon", size=1.5, rew=["xp:100", "create:andesite_alloy*16"], desc=[
        "Create'te elektrik yok; her şey &edönme gücüyle&r çalışır. Bir şeyi döndürürsün, o dönüş miller ve dişlilerle makinelere aktarılır. Hemen hemen her parçanın temeli &eAndesite Alloy&r: andezit ile demir parçacıklarını (iron nugget) çalışma masasında birleştirerek yaparsın. Bolca yap, çok lazım olacak.",
    ]),
    Q("cr_shaft", ["create:shaft*8", "create:cogwheel*4"], title="Shaft ve Cogwheel", deps=["cr_alloy"], desc=[
        "&eShaft&r dönüşü düz bir hat boyunca taşır, &eCogwheel&r ise yan yana duran dişlilere aktarır. Büyük ve küçük dişliyi birbirine bağlarsan hız ikiye katlanır ya da yarıya düşer. Hangi yöne döndüğünü görmek için bloklara bakabilirsin; ileride alacağın &eEngineer's Goggles&r ile hızları ve yükleri de görürsün. Blokları döndürmek ya da sökmek için &eWrench&r çok işine yarar.",
    ]),
    Q("cr_goggles", ["create:goggles", "create:wrench"], title="Goggles ve Wrench", deps=["cr_shaft"], desc=[
        "&eEngineer's Goggles&r'ı kafana tak: makinelere baktığında ne kadar hızlı döndüklerini ve ne kadar &eStress&r (yük) kullandıklarını gösterir. Her güç kaynağının bir kapasitesi vardır; bağladığın makinelerin toplam yükü bunu aşarsa her şey durur. &eWrench&r ile blokları sağ tıklayarak döndürür, Shift + sağ tık ile anında sökersin. Bu ikisi Create'te en çok kullanacağın aletler.",
    ]),
    Q("cr_wheel", "create:water_wheel", deps=["cr_shaft"], rew=["xp:100"], desc=[
        "İlk güç kaynağın &eWater Wheel&r olsun. Akan suyun yanına koy, su çarkın kanatlarına çarptıkça döner ve ortasındaki şaftı çevirir. Ne kadar çok kanadına su değerse o kadar iyi çalışır. Daha fazla güç için birden fazla çarkı aynı şafta dizebilir ya da ileride &eWindmill Bearing&r ile yel değirmeni kurabilirsin. Başlangıç için ufak bir El Krankı (&eHand Crank&r) da işini görür.",
    ]),
    Q("cr_press", ["create:mechanical_press", "create:iron_sheet*8"], title="Mechanical Press", deps=["cr_wheel"], desc=[
        "&eMechanical Press&r yukarıdan aşağı vurarak eşyaları ezer. Altına bir &eDepot&r koyup üzerine demir külçe bırakırsan &eIron Sheet&r yapar. Plakalar Create'teki birçok tarifte lazım. Press'i bir &eBasin&r'in üstüne koyarsan eşyaları sıkıştırır (örneğin 9 külçeyi bloğa çevirir). Depot'un yerine yürüyen bant koyarsan bant üstünden geçen her şeyi otomatik işler.",
    ]),
    Q("cr_belt", ["create:belt_connector*4", "create:depot"], title="Bantlar ve Depot", deps=["cr_wheel"], desc=[
        "&eMechanical Belt&r iki şaftı birbirine bağlayan yürüyen banttır: bir şafta sağ tıkla, sonra diğerine sağ tıkla, aradaki bant oluşur. Üstüne koyduğun eşyaları taşır, Press, Saw veya Fan gibi makinelerin altından geçirerek &eotomatik üretim hattı&r kurmanı sağlar. &eDepot&r ise tek bir eşyayı tutan küçük bir masadır, makinelerin altında iş masası gibi kullanılır.",
    ]),
    Q("cr_mixer", ["create:mechanical_mixer", "create:basin"], title="Mixer ve Basin", deps=["cr_press"], desc=[
        "&eBasin&r bir karıştırma kabı. Üstüne &eMechanical Mixer&r koyarsan içine attığın malzemeleri karıştırıp yeni şeyler yapar: örneğin andezit ve demir parçacığından otomatik Andesite Alloy. Bazı tarifler &eısı&r ister; Basin'in altına bir &eBlaze Burner&r koyup içine yakıt verirsen ısınır. JEI'de Mixer tariflerinin altında alev simgesi varsa ısı gerekiyordur.",
    ]),
    Q("cr_mill", "create:millstone", deps=["cr_wheel"], desc=[
        "&eMillstone&r eşyaları öğütür: içine çakıl atarsan çakmaktaşı, buğday atarsan un, cevher atarsan &eCrushed Ore&r verir. Crushed Ore'u eritmek normal cevherden daha fazla külçe demektir. Daha hızlı ve verimli öğütme için ileride iki &eCrushing Wheel&r'i yan yana koyup ters yönlerde döndürebilirsin.",
    ]),
    Q("cr_fan", "create:encased_fan", title="Encased Fan: Toplu İşleme", deps=["cr_mill", "cr_belt"], desc=[
        "&eEncased Fan&r rüzgar üfler; önüne ne koyduğuna göre eşyaları toplu halde işler. Önüne &esu&r koyarsan üflediği hava eşyaları yıkar (Crushed Ore yıkanınca ekstra parçacık verir), &elav ya da ateş&r koyarsan eritir veya pişirir, &ekamp ateşi&r koyarsan tüttürür. Yere attığın ya da bant üstünde geçen eşyaların hepsi aynı anda işlenir. Tek fırında tek tek pişirmekten çok daha hızlı!",
    ]),
    Q("cr_brass", "create:brass_ingot*8", deps=["cr_mixer"], rew=["xp:150", "create:brass_ingot*8"], desc=[
        "Create'in ikinci aşaması &eBrass Ingot&r ile başlar. Çinko cevheri (Zinc Ore) dünyada, genelde derinlerde bulunur. Bakır ve çinko külçeyi ısıtılmış bir Basin'de Mixer ile karıştırınca Brass çıkar. Bunun için Basin'in altına bir &eBlaze Burner&r koy ve içine yakıt ver. Blaze Burner için Nether'de bir Blaze'i boş bir burner ile yakalaman gerekiyor; JEI'den bak.",
    ]),
    Q("cr_tube", "create:electron_tube*4", deps=["cr_brass"], desc=[
        "&eElectron Tube&r daha gelişmiş makinelerin parçası. Rose Quartz'ı (kuvars ve kızıltaşla yapılır) bir zımparayla parlatıp (Sandpaper ile sağ tık ya da Deployer ile) &ePolished Rose Quartz&r yaparsın, sonra Iron Sheet ile birleştirirsin. Brass Casing ve Electron Tube birlikte bir sürü akıllı makineyi açar.",
    ]),
    Q("cr_deployer", "create:deployer", deps=["cr_tube"], desc=[
        "&eDeployer&r bir robot kol gibidir: elindeki eşyayla önündeki bloğa sağ ya da sol tık yapar. Blok koyabilir, eşya kullanabilir, hayvanları besleyebilir, hatta bant üstündeki eşyalara bir şeyler &emonte edebilir&r. En önemli işi bir sonraki görevdeki sıralı montaj; tek bir parçayı adım adım birçok makineden geçirerek karmaşık eşyalar yapmak.",
    ]),
    Q("cr_precision", "create:precision_mechanism*2", deps=["cr_deployer"], rew=["xp:250", "create:precision_mechanism"], desc=[
        "&ePrecision Mechanism&r ilk &esıralı montaj&r (Sequenced Assembly) tarifin. Bir Golden Sheet bant üstünde ilerlerken Deployer'lar ona sırayla dişli, büyük dişli ve parçacık takar, en sonda Press bastırır; bu döngü birkaç kez tekrarlanır. JEI'de tarifin her adımını görebilirsin. Bazen montaj bozulup çöp çıkarır, bu normal. Bu mekanizma trenler, Mechanical Arm ve daha birçok ileri parça için lazım.",
    ]),
    Q("cr_arm", "create:mechanical_arm", deps=["cr_precision"], desc=[
        "&eMechanical Arm&r bir yerden eşya alıp başka bir yere koyar. Yerleştirmeden önce elinde tutarken alacağı ve bırakacağı yerlere sağ tıklayarak seçersin (mavi alma, turuncu bırakma). Sandıktan makineye, makineden banta, Depot'tan Depot'a; fabrikandaki elle taşıma işlerinin çoğunu yapar.",
    ]),
    Q("cr_steam", ["create:steam_engine", "create:fluid_tank*4"], title="Steam Engine: Büyük Güç", deps=["cr_brass"], rew=["xp:250"], desc=[
        "Su çarkları büyük fabrikalara yetmez. Birkaç &eFluid Tank&r'ı yan yana koyup içine su pompala, altına ısıtılmış &eBlaze Burner&r'lar koy ve tankın yanına &eSteam Engine&r yapıştır: kazan haline gelir ve çok güçlü bir dönme kaynağı olur. Tanka baktığında Goggles ile kazanın seviyesini ve neyin eksik olduğunu (su mu, ısı mı) görürsün.",
    ]),
    Q("cr_train", ["create:track*32", "create:track_station", "create:controls"], title="Trenler", deps=["cr_precision"], shape="gear", size=1.5, rew=["xp:400"], desc=[
        "Create'in en havalı kısmı: &etrenler&r. Ray (Track) döşe, raya bir &eTrain Station&r koy, istasyonun önüne Train Casing bloklarıyla bir tren gövdesi yap ve üzerine &eControls&r ile bir koltuk ekle, sonra istasyonun menüsünden treni birleştir. Treni elle sürebilir ya da &eSchedule&r ile istasyonlar arasında kendi kendine gidip gelmesini sağlayabilirsin. Arkadaşlarınla üsler arasına demiryolu döşemek çok keyifli!",
    ]),
])

create_addons = Chapter("create_addons", "Create Eklentileri", "createaddition:electric_motor", "tech", sub="Create'i elektrikle ve büyüyle birleştir", quests=[
    Q("ca_intro", "check", title="Create'in Yardımcıları", shape="hexagon", size=1.5, desc=[
        "Bu sayfadaki modlar Create'e yeni makineler ekliyor. &eCreate Crafts & Additions&r dönme gücü ile elektriği birbirine çevirir, &eCreate Enchantment Industry&r tecrübe (XP) ve büyülemeyi otomatikleştirir, &eCreate Dragons Plus&r ise toplu işleme ve sıvılarla ilgili yeni yollar açar. Önce Create sayfasında biraz ilerlemen iyi olur.",
    ]),
    Q("ca_wire", ["createaddition:copper_wire*8", "createaddition:connector*4"], title="Kablolar ve Bağlantılar", deps=["ca_intro"], desc=[
        "Elektriği taşımak için &eConnector&r'ları makinelere ya da bloklara yerleştir, sonra elinde &eCopper Spool&r (bakır tel makarası) varken bir connector'dan diğerine sağ tıkla: aralarına kablo çekilir. Böylece elektriği uzak mesafelere taşıyabilirsin. Teller ve plakalar için &eRolling Mill&r kullanılır.",
    ]),
    Q("ca_alternator", "createaddition:alternator", deps=["ca_wire"], desc=[
        "&eAlternator&r dönme gücünü &eelektriğe&r (FE) çevirir. Bir şaftla döndür, elektrik üretmeye başlasın. Böylece Create ile kurduğun su çarkı ya da buhar motoru, Mekanism ya da Powah makinelerini de çalıştırabilir. Elektriği saklamak için &eModular Accumulator&r kullan.",
    ]),
    Q("ca_motor", "createaddition:electric_motor", deps=["ca_alternator"], desc=[
        "&eElectric Motor&r tam tersini yapar: elektrik alır ve dönme gücü verir. Hızını menüsünden ayarlarsın. Büyük bir enerji sistemin varsa su çarklarıyla uğraşmadan Create makinelerine güç verebilirsin. Elektrikle çalışan bir Create fabrikası için birebir.",
    ]),
    Q("ca_tesla", "createaddition:tesla_coil", deps=["ca_motor"], optional=True, desc=[
        "&eTesla Coil&r elektriği kablosuz olarak yakındaki eşyalara aktarır: altındaki Depot'a koyduğun pil ya da enerjili aletleri şarj eder. Bazı tarifler de Tesla Coil ile 'şarj edilerek' yapılır, JEI'de bak.",
    ]),
    Q("cei_xp", ["create_enchantment_industry:mechanical_grindstone", "create_enchantment_industry:experience_bucket"], title="Sıvı Tecrübe", deps=["ca_intro"], desc=[
        "&eCreate Enchantment Industry&r tecrübeyi (XP) bir &esıvıya&r çevirir. &eMechanical Grindstone&r ile büyülü eşyaları öğüterek ya da mob çiftliklerinden XP toplayarak bu sıvıyı elde edersin. Sıvı XP'yi borularla taşıyabilir, tanklarda saklayabilir ve makinelerde kullanabilirsin. Kovaya da doldurulabilir.",
    ]),
    Q("cei_enchanter", "create_enchantment_industry:blaze_enchanter", deps=["cei_xp"], rew=["xp:250"], desc=[
        "&eBlaze Enchanter&r, sıvı XP harcayarak eşyaları otomatik büyüler. İçine bir &eEnchanting Template&r koyarak hangi büyüyü yapacağını seçersin. Bant üstünden geçen bütün kılıçları, kazmaları ya da kitapları aynı büyüyle büyüleyebilirsin. Enchanting masasında şans oyunu oynamak istemiyorsan harika bir seçenek.",
    ]),
    Q("cei_printer", "create_enchantment_industry:printer", deps=["cei_xp"], optional=True, desc=[
        "&ePrinter&r kitapları ve haritaları kopyalar; büyülü kitapları da sıvı XP harcayarak çoğaltabilir. Takım arkadaşların için aynı büyülü kitaptan birkaç tane yapmak istersen işine yarar.",
    ]),
    Q("cdp_hatch", "create_dragons_plus:fluid_hatch", deps=["ca_intro"], optional=True, desc=[
        "&eCreate Dragons Plus&r küçük ama kullanışlı eklemeler yapar. &eFluid Hatch&r ile sıvıları kolayca Basin gibi makinelere aktarabilirsin. Ayrıca Encased Fan'a yeni toplu işleme türleri ekler (örneğin Ender Dragon nefesi ile işleme). Yeni tarifleri JEI'de 'Create Dragons Plus' altında bulabilirsin.",
    ]),
])

ie = Chapter("immersive_engineering", "Immersive Engineering", "immersiveengineering:hammer", "tech", sub="Endüstri devrimi: çok bloklu makineler ve kablolar", quests=[
    Q("ie_hammer", ["immersiveengineering:hammer", "immersiveengineering:manual"], title="Engineer's Hammer ve Manual", shape="hexagon", size=1.5, rew=["xp:100"], desc=[
        "Immersive Engineering'in makineleri çoğunlukla &eçok bloklu yapılar&r (multiblock): blokları belli bir şekilde dizersin, sonra &eEngineer's Hammer&r ile sağ tıklarsın ve yapı makineye dönüşür. Hangi bloğu nereye koyacağını &eEngineer's Manual&r gösterir; kitabı açıp makinenin sayfasına bak, 3 boyutlu bir modeli bile var. Çekiç ayrıca cevherleri toz haline getirmek için de kullanılır.",
    ]),
    Q("ie_coke", ["immersiveengineering:cokebrick*27", "immersiveengineering:coal_coke*8"], title="Coke Oven", deps=["ie_hammer"], desc=[
        "İlk makinen &eCoke Oven&r: 27 adet &eCoke Brick&r ile 3x3x3 bir küp yap ve ön yüzün ortasına çekiçle vur. İçine kömür koyarsan yavaşça &eCoal Coke&r ve &eCreosote Oil&r üretir. Coal Coke çelik yapmak için, Creosote ise ahşabı işlemek için lazım. Fırın sıvıyı içinde saklar, bir kovayla çıkarabilirsin.",
    ]),
    Q("ie_wood", "immersiveengineering:treated_wood_horizontal*16", title="Treated Wood", deps=["ie_coke"], desc=[
        "Normal tahtaları ortaya koyup Creosote kovasıyla çevrelersen &eTreated Wood&r elde edersin. Bu çürümeyen, yanmayan özel bir tahta. IE'nin rüzgar ve su değirmenlerinden çitlerine, birçok yapı parçası Treated Wood'dan yapılır.",
    ]),
    Q("ie_power", ["immersiveengineering:watermill", "immersiveengineering:dynamo"], title="Su Değirmeni ve Dynamo", deps=["ie_wood"], rew=["xp:150"], desc=[
        "IE'de elektrik üretmenin ilk yolu: akan suya bir &eWater Wheel&r (ya da açık havaya bir &eWindmill&r) koy ve arkasına bir &eKinetic Dynamo&r yerleştir. Değirmen döndükçe dynamo elektrik üretir. Su değirmeni akıntının hızına, yel değirmeni yüksekliğe ve etrafındaki boşluğa göre daha iyi çalışır.",
    ]),
    Q("ie_wire", ["immersiveengineering:wirecoil_copper*4", "immersiveengineering:connector_lv*4", "immersiveengineering:capacitor_lv"], title="Kablolar ve Kapasitör", deps=["ie_power"], desc=[
        "IE'de elektrik direklerle taşınır. Makinelere &eLV Connector&r tak, elinde &eCopper Wire Coil&r varken bir connector'a, sonra diğerine sağ tıkla; aralarına gerçek bir kablo çekilir. &eLV Capacitor&r elektriği depolar. Dikkat: LV kablolar düşük gerilim taşır; daha yüksek gerilim (MV, HV) için farklı kablolar gerekir, aksi halde kablo yanar. Kabloları &eWirecutter&r ile kesebilirsin.",
    ]),
    Q("ie_steel", "immersiveengineering:ingot_steel*8", deps=["ie_coke"], rew=["xp:200", "immersiveengineering:ingot_steel*8"], desc=[
        "&eBlast Furnace&r: Fire Brick'lerle (Blast Brick) 3x3x3 bir yapı kur ve çekiçle vur. İçine demir ve Coal Coke koyarsan &eSteel Ingot&r üretir. Çelik IE'nin en önemli malzemesi; gelişmiş makinelerin neredeyse hepsi çelik ister. Biraz yavaştır, birkaç fırını yan yana kurabilirsin.",
    ]),
    Q("ie_workbench", "immersiveengineering:workbench", title="Engineer's Workbench", deps=["ie_steel"], desc=[
        "&eEngineer's Workbench&r IE'nin silah ve alet masasıdır. Burada &eRevolver&r, &eMining Drill&r ve bunların geliştirmelerini yaparsın: daha fazla mermi, daha hızlı kazma, su altında çalışma gibi. Matkap kafaları zamanla aşınır, yedek bulundur.",
    ]),
    Q("ie_engineering", ["immersiveengineering:light_engineering*8", "immersiveengineering:heavy_engineering*4"], title="Mühendislik Blokları", deps=["ie_steel", "ie_wire"], desc=[
        "Büyük makineler bu bloklardan yapılır: &eLight Engineering Block&r ve &eHeavy Engineering Block&r. Bunlar demir/çelik parçalar ve mekanik bileşenlerle yapılır. Bir sonraki adım olan Crusher ve diğer büyük makineler için bolca hazırla.",
    ]),
    Q("ie_crusher", "check", title="Crusher Kur", shape="gear", size=1.5, deps=["ie_engineering"], rew=["xp:300"], desc=[
        "&eCrusher&r cevherleri toz haline getirip &eher cevherden 2 külçe&r almanı sağlar. Kılavuzdaki (Engineer's Manual) yapıyı kur ve çekiçle vur, sonra elektrik bağla. Üstündeki hazneye attığın her şeyi öğütür. Bu yapıyı kurunca IE'nin ileri seviye makinelerine (Arc Furnace, Excavator, Refinery) hazırsın; hepsini kılavuzda bulabilirsin. Kurduktan sonra bu görevi işaretle.",
    ]),
])

mek = Chapter("mekanism", "Mekanism", "mekanism:steel_casing", "tech", sub="Cevher çoğaltma, makineler ve ötesi", quests=[
    Q("mk_osmium", "mekanism:ingot_osmium*8", shape="hexagon", size=1.5, rew=["xp:100"], desc=[
        "Mekanism'in temel metali &eOsmium&r. Mavimsi gri cevherini dünyada demir gibi bulursun; erittiğinde Osmium Ingot verir. Mekanism makinelerinin neredeyse hepsi osmiyum ister, bolca topla. Mekanism'de her şey &eelektrikle&r çalışır, bu yüzden makinelerden önce bir jeneratöre ihtiyacın olacak.",
    ]),
    Q("mk_infuser", "mekanism:metallurgic_infuser", deps=["mk_osmium"], desc=[
        "&eMetallurgic Infuser&r, Mekanism'deki ilk makinen. Bir malzemeyi başka bir şeyle 'aşılar': demir + kömür = &eSteel&r, osmiyum + kızıltaş = &eInfused Alloy&r gibi. Sol yuvaya aşılayacağın maddeyi (kömür, kızıltaş, elmas...) koyar, ortaya ana malzemeyi koyarsın. Makinelerin yan yüzlerini menüdeki ayar sekmesinden ayarlayabilirsin.",
    ]),
    Q("mk_gen", "mekanismgenerators:heat_generator", deps=["mk_osmium"], rew=["xp:100"], desc=[
        "Makineler elektrik ister. İlk jeneratör olarak &eHeat Generator&r iyi bir seçim: içine kömür ya da odun koyarsan yakar, yanına lav koyarsan lavdan da ısı alır. Gündüzleri &eSolar Generator&r, yükseklerde &eWind Generator&r da kullanabilirsin. Elektriği makinelere taşımak için bir sonraki görevdeki kablolar lazım.",
    ]),
    Q("mk_cable", ["mekanism:basic_universal_cable*8", "mekanism:configurator"], title="Universal Cable ve Configurator", deps=["mk_gen"], desc=[
        "&eUniversal Cable&r elektriği jeneratörden makinelere taşır; kablolar otomatik olarak yanındaki bloklara bağlanır. Eşya için &eLogistical Transporter&r, sıvı için &eMechanical Pipe&r, gaz için &ePressurized Tube&r var. &eConfigurator&r ile makinelerin hangi yüzünün giriş, hangisinin çıkış olduğunu ayarlar, Shift + sağ tık ile kabloların bağlantısını açıp kapatırsın.",
    ]),
    Q("mk_steel", ["mekanism:ingot_steel*8", "mekanism:steel_casing"], title="Steel Casing", deps=["mk_infuser"], rew=["xp:150", "mekanism:steel_casing"], desc=[
        "Infuser'da demir ve kömürle önce Enriched Iron, sonra &eSteel&r yap. Çelik ve osmiyumdan yapılan &eSteel Casing&r bütün Mekanism makinelerinin gövdesi. Makine kurmaya başlamadan önce birkaç tane hazırla. Ayrıca çok kullanacağın &eBasic Control Circuit&r'ı da Infuser'da yaparsın.",
    ]),
    Q("mk_enrich", "mekanism:enrichment_chamber", title="2x: Enrichment Chamber", deps=["mk_steel", "mk_cable"], rew=["xp:200"], desc=[
        "Mekanism'in en büyük gücü &ecevher çoğaltma&r. İlk adım &eEnrichment Chamber&r: bir cevheri koyduğunda 2 toz verir, tozu eritince 2 külçe olur. Yani madenden getirdiğin her cevher &e2 kat&r külçe demek. Ayrıca bu makine başka işler de yapar, JEI'ye bak. Bir sonraki adımlarda bu oranı 3, 4 ve 5 kata çıkaracağız.",
    ]),
    Q("mk_purify", "mekanism:purification_chamber", title="3x: Purification Chamber", deps=["mk_enrich"], rew=["xp:250"], desc=[
        "&ePurification Chamber&r oksijen gazı harcayarak cevherleri &e3 kat&r verimle işler: cevher → Clump → Dirty Dust → Dust → külçe. Oksijeni &eElectrolytic Separator&r ile sudan elde edersin (su, hidrojen ve oksijene ayrılır). Makineleri yan yana dizip birinin çıkışını diğerinin girişine bağlayarak bir işleme hattı kurmalısın.",
    ]),
    Q("mk_inject", "mekanism:chemical_injection_chamber", title="4x: Chemical Injection", deps=["mk_purify"], rew=["xp:300"], desc=[
        "&eChemical Injection Chamber&r hidrojen klorür gazı ile cevherleri &e4 kat&r verimle işler; Purification hattının önüne eklenir. Gaz üretmek için tuz (Salt) ve birkaç ek makine gerekiyor. Burası biraz karışıklaşmaya başlar; JEI'de her ürünün nereden geldiğine (U tuşu) bakarak adım adım ilerle. Sonraki seviye (5x) için Chemical Dissolution Chamber ve Chemical Washer gerekiyor.",
    ]),
    Q("mk_upgrade", ["mekanism:upgrade_speed", "mekanism:upgrade_energy"], title="Makine Upgrade'leri", deps=["mk_enrich"], optional=True, desc=[
        "Mekanism makinelerinin sağ tarafında upgrade yuvaları var. &eSpeed Upgrade&r makineyi hızlandırır ama daha fazla elektrik harcatır, &eEnergy Upgrade&r enerji tüketimini düşürür. İkisini birlikte kullanmak en iyisi. Ayrıca makineleri Basic'ten Advanced, Elite ve Ultimate seviyeye &eTier Installer&r ile yükseltip aynı anda birden fazla eşya işletebilirsin.",
    ]),
    Q("mk_disassembler", "mekanism:atomic_disassembler", deps=["mk_steel"], rew=["xp:200"], desc=[
        "&eAtomic Disassembler&r elektrikle çalışan süper bir alet: kazma, kürek ve balta bir arada, üstelik silah olarak da iyi. Shift + sağ tık ile modunu değiştirip bir anda birden çok blok kırabilirsin. Şarj etmek için bir enerji küpüne ya da şarj cihazına koy.",
    ]),
    Q("mk_tools", "mekanismtools:osmium_paxel", title="Mekanism Tools", deps=["mk_osmium"], optional=True, desc=[
        "&eMekanism Tools&r yeni metal türlerinden zırh ve aletler ekler: osmiyum, bronz, çelik, Refined Obsidian ve Refined Glowstone. En kullanışlısı &ePaxel&r; kazma, balta ve kürek tek alette. Refined Obsidian seti oyunun en güçlü zırhlarından biri.",
    ]),
])

powah = Chapter("powah", "Powah!", "powah:energizing_orb", "tech", sub="Kolay ve güçlü enerji", quests=[
    Q("pw_paste", "powah:dielectric_paste*16", shape="hexagon", size=1.5, desc=[
        "Powah! enerji üretmenin ve saklamanın basit yollarını sunar. Her şey &eDielectric Paste&r ile başlar: kömür, kil ve lav kovası (ya da Blaze Powder) ile yapılır. Bu macundan &eDielectric Rod&r ve &eDielectric Casing&r yaparsın; Powah'taki makinelerin hepsinin ana parçaları bunlar.",
    ]),
    Q("pw_orb", ["powah:energizing_orb", "powah:energizing_rod_starter*2"], title="Energizing Orb", deps=["pw_paste"], rew=["xp:150"], desc=[
        "&eEnergizing Orb&r Powah'ın kalbi. Orb'u yere koy, etrafına (birkaç blok mesafe içinde ve orb'u görecek şekilde) &eEnergizing Rod&r'lar yerleştir ve rod'lara elektrik ver. Orb'a sağ tıklayıp malzemeleri koyduğunda rod'lar onlara enerji yükler ve yeni eşyalar çıkar. Örneğin demir + altın = &eEnergized Steel&r. Ne kadar çok rod, o kadar hızlı.",
    ]),
    Q("pw_gen", "powah:furnator_starter", title="İlk Jeneratör", deps=["pw_paste"], rew=["xp:100"], desc=[
        "Orb'a güç vermek için bir jeneratör lazım. &eFurnator&r içine attığın kömür ve odunu yakarak elektrik üretir. Alternatif olarak &eSolar Panel&r gündüzleri bedava enerji verir, &eThermo Generator&r ise altına lav ve yanına soğutucu (su, buz) koyunca çalışır. Hepsi Starter seviyesinden başlayıp kristallerle yükseltilebilir.",
    ]),
    Q("pw_cell", ["powah:energy_cell_starter", "powah:energy_cable_starter*8"], title="Energy Cell ve Cable", deps=["pw_gen"], desc=[
        "&eEnergy Cell&r elektrik depolayan bir pildir, &eEnergy Cable&r ise elektriği taşır. Jeneratörden hücreye, hücreden makinelere kablo çek. Gece güneş paneli çalışmazken hücredeki enerji makinelerini çalıştırmaya devam eder. Powah kabloları diğer modların makinelerine de bağlanır.",
    ]),
    Q("pw_blazing", "powah:crystal_blazing*4", deps=["pw_orb"], desc=[
        "Orb'a Blaze Powder koyarak &eBlazing Crystal&r yap. Kristaller Powah'ta seviye atlamanın anahtarı: Starter → Basic → Hardened → Blazing → Niotic → Spirited → Nitro. Her yeni kristal ile jeneratörlerin, hücrelerin ve kabloların daha güçlü sürümlerini yapabilirsin.",
    ]),
    Q("pw_niotic", "powah:crystal_niotic*4", deps=["pw_blazing"], desc=[
        "&eNiotic Crystal&r, Orb'da &eelmas&r enerjiyle doldurularak yapılır. Daha fazla enerji ister, o yüzden önce rod ve jeneratörlerini yükseltmek isteyebilirsin. Niotic seviyesi makineler başlangıç seviyesine göre çok daha güçlüdür.",
    ]),
    Q("pw_spirited", "powah:crystal_spirited*4", deps=["pw_niotic"], desc=[
        "&eSpirited Crystal&r, Orb'da &ezümrüt&r ile yapılır. Bu seviyedeki jeneratörler artık ciddi bir üssü tek başına besleyebilir. Bir sonraki adım olan Nitro Crystal için çok daha fazla enerji gerekiyor.",
    ]),
    Q("pw_nitro", "powah:crystal_nitro*2", deps=["pw_spirited"], rew=["xp:300"], desc=[
        "&eNitro Crystal&r Powah'ın en üst seviyesi. Nether Star gibi pahalı malzemeler ve büyük miktarda enerji ister. Nitro seviye bir &eReactor&r ya da güneş paneli devasa miktarda enerji üretir. Buraya ulaştıysan enerji derdin bitti demektir!",
    ]),
    Q("pw_reactor", "powah:reactor_starter*36", title="Reactor", shape="gear", size=1.5, deps=["pw_blazing"], rew=["xp:400"], desc=[
        "&eReactor&r Powah'ın en güçlü jeneratörü. 36 adet Reactor bloğunu 3x3x4 bir sütun şeklinde dizersin, yapı kendiliğinden birleşir. İçine &eUraninite&r (yer altında parlayan yeşil cevher) yakıt olarak koyarsın. Reaktör ısınır; soğutmak için su, buz ya da Dry Ice ver, aksi halde verim düşer. Dikkatli kurarsan çok büyük enerji üretir.",
    ]),
])

integrated = Chapter("integrated_dynamics", "Integrated Dynamics", "integrateddynamics:logic_programmer", "tech", sub="Mantık ağları, otomasyon ve depolama erişimi", quests=[
    Q("id_menril", "integrateddynamics:menril_sapling", shape="hexagon", size=1.5, desc=[
        "Integrated Dynamics bir &emantık ve otomasyon&r modu; biraz programlamaya benzer ama korkmana gerek yok. Her şey mavi yapraklı &eMenril&r ağacıyla başlar; bunları genelde ormanlık biyomlarda görürsün. Fidanını alıp kendi ağaç tarlanı kur. Menril odunundan çıkan reçine (resin) modun ana malzemesi.",
    ]),
    Q("id_squeezer", ["integrateddynamics:squeezer", "integrateddynamics:drying_basin"], title="Squeezer ve Drying Basin", deps=["id_menril"], desc=[
        "&eSqueezer&r'ın içine Menril odunu koy ve üstüne zıplayarak ez: &eMenril Resin&r adlı bir sıvı çıkar. Bu sıvıyı &eDrying Basin&r'e aktarırsan kuruyup &eCrystalized Menril Chunk&r'a dönüşür. Bu kristaller kabloların ve parçaların temel malzemesi. İleride bu işi otomatik yapan mekanik sürümleri de var.",
    ]),
    Q("id_cable", "integrateddynamics:cable*16", title="Logic Cable", deps=["id_squeezer"], desc=[
        "&eLogic Cable&r bütün parçaları birbirine bağlayan ağ kablosu. Kabloya &epart&r denen küçük modüller takarsın: okuyucular (reader) bir şeyi ölçer, yazıcılar (writer) bir şeyi değiştirir, ekranlar (display) bilgi gösterir. Hepsi aynı kablo ağına bağlıysa birbirleriyle konuşabilirler. Kabloları &eWrench&r ile söküp düzenleyebilirsin.",
    ]),
    Q("id_variable", ["integrateddynamics:variable*8", "integrateddynamics:variablestore"], title="Variable Card", deps=["id_cable"], desc=[
        "&eVariable Card&r, bir bilgiyi taşıyan kart. Örneğin 'sandıktaki demir sayısı' ya da 'gündüz mü' gibi. Okuyuculardan aldığın değeri boş bir karta yazarsın, sonra bu kartı başka parçalarda kullanırsın. Kartları ağda saklamak için &eVariable Store&r kullanılır; kart içindeki bilgi ağda herkes tarafından okunabilir.",
    ]),
    Q("id_reader", ["integrateddynamics:part_inventory_reader", "integrateddynamics:part_display_panel"], title="Reader ve Display Panel", deps=["id_variable"], rew=["xp:150"], desc=[
        "İlk projen: bir sandığın yanına kablo çek, kabloya &eInventory Reader&r tak ve sandığa baksın. Okuyucunun menüsünden bir bilgi seç (örneğin toplam eşya sayısı) ve bir Variable Card'a yaz. Sonra bir &eDisplay Panel&r tak ve kartı içine koy: panel sandıktaki sayıyı canlı gösterir! Aynı mantıkla enerji, sıvı, zaman ve daha birçok şeyi ölçebilirsin.",
    ]),
    Q("id_programmer", "integrateddynamics:logic_programmer", deps=["id_variable"], rew=["xp:150"], desc=[
        "&eLogic Programmer&r, kartlara mantık işlemleri yazmanı sağlar: 'eğer sandıkta 64'ten az demir varsa' gibi koşullar, toplama-çıkarma, karşılaştırmalar. Bu sonuçları redstone yazıcılarına bağlayarak makineleri açıp kapatabilirsin. Başta karışık gelebilir; modun içindeki kılavuz kitabında (&eOn the Dynamics of Integration&r) adım adım öğreticiler var.",
    ]),
    Q("it_tunnels", ["integratedtunnels:part_interface_item*2", "integratedtunnels:part_exporter_item"], title="Integrated Tunnels", deps=["id_cable"], rew=["xp:150"], desc=[
        "&eIntegrated Tunnels&r aynı kablo ağıyla eşya, sıvı ve enerji taşımanı sağlar. Sandıklara &eItem Interface&r takarsan ağa bağlanırlar. &eItem Exporter&r ağdaki eşyaları bir yere aktarır, &eImporter&r bir yerden çeker. Filtreler için Variable Card kullanılır; örneğin 'sadece cevherleri fırına gönder'. Boru döşemeden her şeyi bir kabloyla taşıyabilirsin.",
    ]),
    Q("it_terminal", "integratedterminals:part_terminal_storage", title="Storage Terminal", deps=["it_tunnels"], shape="gear", size=1.5, rew=["xp:250"], desc=[
        "&eStorage Terminal&r (Integrated Terminals), ağa bağlı bütün sandıkların içeriğini tek bir ekranda gösterir. Buradan herhangi bir sandıktaki eşyayı arayıp alabilir, eşyaları içeri atabilir, hatta tarif yapabilirsin. Taşınabilir sürümüyle de üssün içinde her yerden erişebilirsin.",
    ]),
])

jdt = Chapter("just_dire_things", "Just Dire Things", "justdirethings:gooblock_tier1", "tech", sub="Goo, yeni metaller ve akıllı aletler", quests=[
    Q("jdt_goo", "justdirethings:gooblock_tier1", shape="hexagon", size=1.5, rew=["xp:100"], desc=[
        "Just Dire Things'in her şeyi &eGoo&r ile başlar: canlı, blokları 'yiyip' dönüştüren tuhaf bir madde. &eGooblock (Tier 1)&r'i kil, şeker, çürük et ve toprakla yaparsın. Goo'nun yanına belli blokları koyduğunda, bir süre sonra onları yeni malzemelere çevirir. Hangi Goo'nun neyi dönüştürdüğünü JEI'de 'Goo Spread' sekmesinde görürsün.",
    ]),
    Q("jdt_ferricore", "justdirethings:ferricore_ingot*8", deps=["jdt_goo"], desc=[
        "Gooblock'un yanına (herhangi bir yüzüne) bir &eIron Block&r koy ve bekle. Birkaç dakika içinde demir bloğu &eRaw Ferricore Ore&r'a dönüşür. Kazıp eritince &eFerricore Ingot&r elde edersin. Ferricore'dan yapılan aletler kendini tamir edebilir ve çeşitli yetenekler kazanabilir.",
    ]),
    Q("jdt_tools", "justdirethings:ferricore_wrench", title="Ferricore Aletleri", deps=["jdt_ferricore"], desc=[
        "Ferricore ile ilk aletlerini yap. JDT aletlerinin özelliği: içlerine &eUpgrade&r koyarak yetenek kazandırabilirsin, örneğin ağacın tamamını kesmek (Tree Feller), cevherleri tek seferde kazmak ya da otomatik eritmek. Aleti elinde tutarken Shift + sağ tık ile ayar ekranını açarsın. Upgrade'lerin listesine JEI'den göz at.",
    ]),
    Q("jdt_goo2", "justdirethings:gooblock_tier2", deps=["jdt_ferricore"], desc=[
        "&eGooblock (Tier 2)&r, Tier 1 Goo'yu Blaze Powder, kızıltaş ve Nether Wart ile güçlendirerek yapılır. Yanına bir &eGold Block&r koyarsan onu &eRaw Blazegold Ore&r'a çevirir. Her seviyedeki Goo bir öncekinin dönüştürdüklerini de dönüştürebilir.",
    ]),
    Q("jdt_blazegold", "justdirethings:blazegold_ingot*8", deps=["jdt_goo2"], desc=[
        "&eBlazegold Ingot&r ikinci seviye metal: aletleri daha güçlü, upgrade yuvaları daha fazla. Blazegold aletleri ateşle ilgili yetenekler de kazanabilir (örneğin kazdığın cevheri anında eritmek). Ayrıca otomasyon makinelerinin (Block Breaker, Block Placer gibi) ikinci seviyeleri için gerekiyor.",
    ]),
    Q("jdt_celestigem", "justdirethings:celestigem*4", deps=["jdt_blazegold"], desc=[
        "Üçüncü seviye Goo, bir &eDiamond Block&r'u &eCelestigem&r cevherine çevirir. Celestigem aletleri çok daha fazla yeteneği aynı anda taşıyabilir. Bu seviyeden sonra ışınlanma silahı (Portal Gun) gibi ilginç eşyalar da açılır.",
    ]),
    Q("jdt_eclipse", "justdirethings:eclipsealloy_ingot*4", deps=["jdt_celestigem"], shape="gear", size=1.5, rew=["xp:400"], desc=[
        "En üst seviye Goo, bir &eNetherite Block&r'u &eEclipse Alloy&r'a çevirir. Eclipse Alloy aletleri JDT'nin en güçlüleri: uçma, ölümsüzlük anları ve zamanla ilgili yetenekler kazanabilirler. Buraya ulaştıysan JDT'yi bitirmiş sayılırsın!",
    ]),
    Q("jdt_machines", ["justdirethings:blockbreakert1", "justdirethings:blockplacert1"], title="Otomasyon Makineleri", deps=["jdt_ferricore"], optional=True, desc=[
        "JDT'nin küçük otomasyon makineleri: &eBlock Breaker&r önündeki bloğu kırar, &eBlock Placer&r blok koyar, &eClicker&r sağ tık yapar, &eSensor&r bir şey algıladığında sinyal verir. Bunları birleştirerek taş üreteci, ağaç kesici gibi basit çiftlikler kurabilirsin. Elektrik gerektirmeyen birinci seviyeleri başlangıç için ideal.",
    ]),
])

pipez = Chapter("pipez", "Pipez", "pipez:item_pipe", "tech", sub="Basit ve hızlı borular", quests=[
    Q("pz_item", "pipez:item_pipe*8", shape="hexagon", size=1.5, desc=[
        "&ePipez&r, eşyaları ve sıvıları bir yerden başka bir yere taşımanın en kolay yolu. &eItem Pipe&r'ı sandıkla makine arasına döşe. Borular kendiliğinden hiçbir yerden çekmez; bir sandıktan çekmesi için eli boşken borunun o sandığa bağlandığı uca &eShift + sağ tık&r yap, o uç 'çekme' (extract) moduna geçer ve rengi değişir. Çekilen eşyalar borunun bağlı olduğu diğer yerlere gider. &ePipe Wrench&r ile de istemediğin bağlantıları koparabilirsin.",
    ]),
    Q("pz_fluid", "pipez:fluid_pipe*8", deps=["pz_item"], desc=[
        "&eFluid Pipe&r su, lav ve diğer modların sıvılarını taşır. Mantık aynı: kaynağa bağlanan uçta çekmeyi açarsın. Örneğin bir su pompasından makinelerine su ya da bir tanktan jeneratöre yakıt taşıyabilirsin.",
    ]),
    Q("pz_energy", "pipez:energy_pipe*8", deps=["pz_item"], desc=[
        "&eEnergy Pipe&r elektrik taşır; farklı modların makinelerini birbirine bağlamak için harika. Jeneratörden çekmeyi aç, enerji bağlı makinelere dağılır. Mekanism, Powah, Create Crafts & Additions gibi modların hepsiyle uyumlu.",
    ]),
    Q("pz_universal", "pipez:universal_pipe*4", deps=["pz_fluid", "pz_energy"], desc=[
        "&eUniversal Pipe&r eşya, sıvı, enerji ve gazı tek boruda taşır. Biraz daha pahalı ama karmaşık kurulumlarda çok yer kazandırır. Hangi türü taşıyacağını ayar ekranından seçebilirsin.",
    ]),
    Q("pz_upgrade", "pipez:basic_upgrade", title="Boru Upgrade'leri", deps=["pz_item"], shape="gear", rew=["xp:150"], desc=[
        "Normal borular yavaştır. Borunun çekme yapan ucuna sağ tıklayıp menüdeki yuvaya &eUpgrade&r takarsan hız ve miktar artar (Basic → Improved → Advanced → Ultimate → Infinity). Upgrade'li borularda &efiltre&r de ayarlayabilir, eşyaların sırayla mı yoksa en yakına mı dağıtılacağını seçebilirsin.",
    ]),
])

TECH = [create, create_addons, ie, mek, powah, integrated, jdt, pipez]
