from engine import Chapter, Q

explore = Chapter("kesif", "Keşif", "naturescompass:naturescompass", "adventure", sub="Yeni biyomlar ve yapılar", quests=[
    Q("ex_intro", "check", title="Dünya Değişti", shape="hexagon", size=1.5, desc=[
        "Bu pakette dünya normal Minecraft'tan çok farklı. &eTerralith&r yüzlerce yeni biyom ve devasa dağlar, kanyonlar ekler. &eYUNG's&r modları zindanları, maden ocaklarını, kaleleri, tapınakları ve Nether kalelerini baştan tasarlar; içleri daha büyük, daha tehlikeli ve daha ödüllüdür. &eTowns & Towers&r ise yeni köy türleri ve kuleler ekler. Gezmeye değer!",
    ]),
    Q("ex_nature", "naturescompass:naturescompass", deps=["ex_intro"], desc=[
        "&eNature's Compass&r istediğin biyomu bulmanı sağlar. Elindeyken sağ tıkla, listeden bir biyom seç (örneğin mantar adası ya da çiçek ormanı) ve pusula seni oraya yönlendirsin. Belli bir biyomda bulunan malzemeleri ararken (örneğin Botania çiçekleri ya da Frostmaw için karlı bölgeler) çok işine yarar.",
    ]),
    Q("ex_explorer", "explorerscompass:explorerscompass", deps=["ex_intro"], desc=[
        "&eExplorer's Compass&r aynı şeyi &eyapılar&r için yapar: zindan, köy, kale, tapınak ya da modların eklediği boss yapıları. Listeden aradığın yapıyı seç, pusula en yakınındakine yönlendirir. Boss avına çıkmadan önce mutlaka yanında bulunsun.",
    ]),
    Q("ex_yung", "check", title="Yeni Zindanlar", deps=["ex_explorer"], rew=["xp:200"], desc=[
        "YUNG's modlarıyla değişen yapılara bir göz at: dev &eStronghold&r'lar, uzun ve dallı &eMineshaft&r'lar, tuzaklı &eDesert/Jungle Temple&r'lar, yeniden tasarlanmış &eNether Fortress&r ve &eOcean Monument&r, bir de iskelet ve zombi dolu yeni &eDungeon&r'lar. Içlerinde iyi ganimet var ama yalnız gitme! Bunlardan birini keşfettiğinde bu görevi işaretle.",
    ]),
    Q("ex_towns", "check", title="Köyler ve Kuleler", deps=["ex_nature"], desc=[
        "&eTowns & Towers&r her biyoma uygun yeni köyler ve yağmacı karakolları ekler; bazı köylerde zaten bir &eWaystone&r bulunur. Bir köy bulup oradaki waystone'u etkinleştirirsen, üssüne kolayca dönebileceğin bir durak noktası edinirsin. Köylülerle takas da etmeyi unutma.",
    ]),
])

apo = Chapter("apotheosis", "Apotheosis", "apotheosis:gem_cutting_table", "adventure", sub="Ganimet, mücevherler ve gelişmiş büyüleme", quests=[
    # --- Kol A: Ekipman ---
    Q("ap_intro", "check", title="Apotheosis Nedir?", shape="hexagon", size=1.5, x=0, y=0, desc=[
        "&eApotheosis&r savaşı ve ganimeti tamamen değiştirir. Düşmanlar ve sandıklar artık &erenkli isimli&r ekipman düşürür: Common (gri), Uncommon (yeşil), Rare (mavi), Epic (mor), Mythic (turuncu). Bu eşyaların rastgele bonusları (&eaffix&r) vardır: ekstra hasar, can çalma, ateş, zırh delme... Ayrıca bazı düşmanlar &eboss&r olarak güçlenmiş halde çıkar. Bu sayfanın üst kolu ekipmanı, alt kolu büyülemeyi anlatıyor.",
    ]),
    Q("ap_gem", ["check"], title="Gem'ler ve Soketler", x=2, y=-2, deps=["ap_intro"], desc=[
        "Bazı ekipmanların &esoketleri&r vardır (eşyanın açıklamasında 'Empty Socket' yazar). Düşmanlardan ve sandıklardan &eGem&r düşer; her gem'in farklı eşya türlerinde farklı bonusu vardır. Gem'i fareyle tutup soketli eşyanın üzerine &esağ tıklarsan&r yerine takılır. Bir gem'i soketine taktığında bu görevi işaretle.",
    ]),
    Q("ap_dust", "apotheosis:gem_dust*8", x=4, y=-2, deps=["ap_gem"], desc=[
        "&eGem Dust&r, Apotheosis masalarının neredeyse hepsinde lazım. İstemediğin gem'leri parçalayarak elde edersin (nasıl yapıldığını JEI'de Gem Dust'a bakıp &eR&r ile gör). Gereksiz gem'leri atma, toza çevir.",
    ]),
    Q("ap_salvage", "apotheosis:salvaging_table", x=6, y=-3, deps=["ap_dust"], desc=[
        "&eSalvaging Table&r istemediğin renkli ekipmanları parçalayıp nadirlik &emalzemelerine&r çevirir; eşyanın nadirliği ne kadar yüksekse o kadar değerli malzeme çıkar. Envanterini dolduran ganimetleri burada eritip bir sonraki adımlarda kullanacağın malzemeleri topla.",
    ]),
    Q("ap_reforge", "apotheosis:simple_reforging_table", title="Reforging Table", x=8, y=-3, deps=["ap_salvage"], rew=["xp:200"], desc=[
        "Beğendiğin bir eşyanın bonusları kötü mü çıktı? &eReforging Table&r'da nadirlik malzemeleri ve Gem Dust harcayarak bonuslarını &eyeniden&r atarsın; birkaç seçenek arasından birini seçersin. &eSimple Reforging Table&r düşük nadirlikler içindir, Netherite ile yapılan normal &eReforging Table&r ise bütün nadirliklerde çalışır.",
    ]),
    Q("ap_cut", "apotheosis:gem_cutting_table", x=6, y=-1, deps=["ap_dust"], desc=[
        "&eGem Cutting Table&r ile aynı türden gem'leri birleştirerek &ekalitesini&r yükseltirsin: Cracked → Chipped → Flawed → Normal → Flawless → Perfect. Yüksek kaliteli gem'ler çok daha güçlü bonus verir. Gem Dust ve nadirlik malzemeleri harcar.",
    ]),
    Q("ap_socket", "apotheosis:sigil_of_socketing", x=8, y=-1, deps=["ap_cut"], desc=[
        "Soketi olmayan ya da az olan bir eşyaya &eSigil of Socketing&r ile soket ekleyebilirsin (Smithing Table'da). Yanlış gem mi taktın? &eSigil of Withdrawal&r gem'leri kırmadan çıkarır. Böylece en sevdiğin kılıcı istediğin gem'lerle donatabilirsin.",
    ]),
    Q("ap_augment", "apotheosis:augmenting_table", x=10, y=-2, deps=["ap_reforge", "ap_socket"], shape="gear", size=1.5, rew=["xp:400"], desc=[
        "&eAugmenting Table&r ekipmanın son aşaması: bir eşyanın tek bir bonusunu seçip güçlendirebilir ya da başka bir bonusla değiştirebilirsin. Nether Star ve Godforged Pearl gibi pahalı malzemeler ister, ama mükemmel ekipmanın son dokunuşu bu.",
    ]),
    Q("ap_spawner", "check", title="Spawner'ları Değiştirmek", x=2, y=-4, deps=["ap_intro"], optional=True, desc=[
        "&eApothic Spawners&r ile canavar spawner'larını &eSilk Touch&r kazmayla kırıp taşıyabilirsin. Spawner'a Shift + sağ tık ile belirli eşyaları kullanarak onu değiştirirsin: daha hızlı doğurma, daha fazla yaratık, oyuncu yokken çalışma gibi. Hangi eşyanın ne yaptığını JEI'de 'Spawner Modifiers' sekmesinde bulursun. Mob çiftlikleri için harika.",
    ]),
    # --- Kol B: Enchanting ---
    Q("en_table", ["apothic_enchanting:weapon_tome", "apothic_enchanting:apothic_enchanting_table"], title="Apothic Enchanting Table", x=2, y=2, deps=["ap_intro"], rew=["lv:10"], desc=[
        "Bu pakette büyüleme masası çok daha derin. Önce bir Önce bir &eTome&r yap (kitap + Blaze Rod; Tome of Weaponry gibi)eTomeÖnce bir &eTome&r yap (kitap + Blaze Rod; Tome of Weaponry gibi)r yap (kitaplar ve Blaze Rod ya da Blaze Powder ile; örneğin Tome of Weaponry) ve onunla &eApothic Enchanting Table&r'ı kur. Masa artık dört değer gösterir:",
        "&eEterna&r: büyünün gücü (seviyesi). En fazla 100.",
        "&eQuanta&r: rastgelelik. Yüksekse sonuç beklenenden çok iyi ya da çok kötü olabilir.",
        "&eArcana&r: nadirlik. Yüksekse daha nadir ve daha çok büyü gelir.",
        "&eClues&r: büyülemeden önce kaç büyüyü önceden görebileceğin.",
        "Bu değerleri masanın etrafına koyduğun raflar belirler. Bu zincir seni adım adım 100'e çıkaracak; ödüller de bol XP, denemekten çekinme!",
    ]),
    Q("en_shelves", "minecraft:bookshelf*15", title="İlk Raflar: Eterna 15", x=4, y=2, deps=["en_table"], rew=["lv:10"], desc=[
        "Masanın etrafına, arada bir blok boşluk bırakıp 15 &eBookshelf&r diz (vanilla'daki gibi). Her raf Eterna'yı artırır ama vanilla raflar seni en fazla &e15&r'e çıkarabilir. Her rafın bir 'en fazla' sınırı vardır; daha yükseğe çıkmak için daha güçlü raflar lazım. Rafın üzerine gelince hangi değerleri verdiğini görürsün.",
    ]),
    Q("en_hell_sea", ["apothic_enchanting:hellshelf*8", "apothic_enchanting:seashelf*8"], title="Hellshelf ve Seashelf: Eterna 45", x=6, y=2, deps=["en_shelves"], rew=["lv:15"], desc=[
        "Bir sonraki seviye için Nether ve okyanus malzemeleri lazım. &eHellshelf&r (Nether tuğlası, Blaze Rod ve Regeneration iksiri) Eterna ve Quanta verir; &eSeashelf&r (prizmarin, kirpi balığı ve su şişesi) Eterna ve Arcana verir. Bu raflar Eterna'yı &e45&r'e kadar çıkarabilir. Her raf 3 Eterna verdiği için 45'e ulaşmak için yaklaşık 15 tane gerekiyor; ikisini karıştırarak dengeli bir masa kur.",
    ]),
    Q("en_infuse", ["apothic_enchanting:infused_hellshelf", "apothic_enchanting:infused_seashelf"], title="Infusion: Rafları Büyüle", x=8, y=2, deps=["en_hell_sea"], rew=["lv:20"], desc=[
        "&eInfusion&r bu modun en önemli tekniği: bazı eşyaları masaya koyduğunda normal büyüler yerine özel bir 'infusion' seçeneği çıkar ve eşya başka bir şeye dönüşür. Bunun için masanın değerleri belli aralıkta olmalı (JEI'de 'Infusion' sekmesinde her tarifin istediği Eterna/Quanta/Arcana yazıyor).",
        "Bir Hellshelf'i Eterna 45, Quanta 30 iken infuse et: &eInfused Hellshelf&r. Bir Seashelf'i Eterna 45, Quanta 15, Arcana 10 iken infuse et: &eInfused Seashelf&r.",
    ]),
    Q("en_xp", "minecraft:experience_bottle*16", title="Kendi XP'ni Üret", x=8, y=4, deps=["en_infuse"], rew=["lv:10", "minecraft:honey_bottle*16"], desc=[
        "Büyülemek bol XP ister, işte bir ipucu: masada bir &eHoney Bottle&r'ı (bal şişesi) infuse edersen &eBottle o' Enchanting&r (XP şişesi) çıkar. Eterna 20 / Quanta 25 / Arcana 25 ile 1 şişe, Eterna 60 ile 8 şişe, Eterna 100 ile 32 şişe verir! Arı kovanı kurup bal toplarsan XP derdin biter. İlk balları ödül olarak veriyoruz.",
    ]),
    Q("en_60", ["apothic_enchanting:blazing_hellshelf", "apothic_enchanting:crystal_seashelf"], title="Gelişmiş Raflar: Eterna 60-65", x=10, y=2, deps=["en_infuse"], rew=["lv:25"], desc=[
        "Infused rafları biraz daha geliştirebilirsin. &eBlazing Hellshelf&r (ateş topu ve Blaze Powder) Eterna'yı &e65&r'e kadar çıkarır ve çok Quanta verir; &eGlowing Hellshelf&r (glowstone) dengelidir. &eCrystalline Seashelf&r (prizmarin kristali) ve &eHeart-Forged Seashelf&r (Heart of the Sea, çok Arcana) &e60&r'a kadar çıkarır. Masanı bunlarla yenile.",
    ]),
    Q("en_tune", ["apothic_enchanting:sightshelf", "check"], title="Ayar Rafları", x=10, y=4, deps=["en_60"], rew=["lv:15"], desc=[
        "Bazen değerleri &edüşürmek&r gerekir, çünkü bazı infusion tarifleri belli bir aralık ister. &eStoneshelf&r Eterna ve Arcana'yı, &eMelonshelf&r Quanta'yı düşürür; &eBeeshelf&r ise Quanta'yı devasa artırır ama Eterna'yı düşürür. &eHellshelf of Sight&r ise &eClues&r verir: büyülemeden önce gelecek büyüleri daha fazla görürsün. Bu rafları ekleyip çıkararak masayı istediğin değerlere ayarla. Sight rafını yapıp masayla oynadıktan sonra işaretle.",
    ]),
    Q("en_deep", ["apothic_enchanting:deepshelf", "apothic_enchanting:echoing_deepshelf"], title="Deepshelf: Eterna 70-75", x=12, y=2, deps=["en_60"], rew=["lv:30"], desc=[
        "Derinlere iniyoruz. Çatlak deepslate karoları ve kitaplarla bir &eDormant Deepshelf&r yap ve onu Eterna 60, Quanta 40, Arcana 40'ta infuse et: &eDeepshelf&r (en fazla &e70&r). Deepshelf'i Echo Shard ve mumlarla &eEchoing Deepshelf&r'a (Arcana) ya da Soul Lantern ve sculk ile &eSoul-Touched Deepshelf&r'a (Quanta) çevirirsen &e75&r'e çıkarsın.",
    ]),
    Q("en_sculk", ["apothic_enchanting:warden_tendril", "apothic_enchanting:echoing_sculkshelf"], title="Sculkshelf: Eterna 80", x=14, y=2, deps=["en_deep"], rew=["lv:35"], desc=[
        "Sırada Ancient City'nin sahibi var: &eWarden&r. Onu yenince &eWarden Tendril&r düşer (çok tehlikeli, takımca gidin!). Tendril, sculk ve Sculk Catalyst ile Echoing ya da Soul-Touched Deepshelf'i &eSculkshelf&r'a yükselt: Eterna &e80&r ve bonus Clues.",
    ]),
    Q("en_end", ["apothic_enchanting:infused_breath*3", "apothic_enchanting:endshelf"], title="Endshelf: Eterna 90", x=16, y=2, deps=["en_sculk"], rew=["lv:40"], desc=[
        "End'e gitme zamanı. Ender Dragon'ın nefesini (boş şişeyle toplanan &eDragon's Breath&r) Eterna 80, Arcana 60 ve Quanta 15-30 arasında infuse et: &eInfused Dragon's Breath&r. Bununla, End taşı tuğlaları ve ender incisiyle &eEndshelf&r yaparsın: Eterna &e90&r. End Rod'larla &ePearlescent Endshelf&r'a yükseltirsen daha dengeli değerler alırsın.",
    ]),
    Q("en_draconic", "apothic_enchanting:draconic_endshelf", title="Draconic Endshelf: Eterna 100", x=18, y=2, deps=["en_end"], shape="gear", size=1.5, rew=["lv:50"], desc=[
        "Son raf: bir Endshelf'i &eDragon Head&r (End şehirlerindeki gemilerde bulunur) ve ender incileriyle &eDraconic Endshelf&r'a çevir. Her biri 20 Eterna verir ve sınırı &e100&r! Masanı 100 Eterna'ya çıkardığında en güçlü büyüleri, normal sınırların üstündeki seviyelerle alabilirsin. Unutma: yüksek seviye büyüler için oyuncu seviyenin de o kadar yüksek olması gerekiyor; bu yüzden ödüller büyük!",
    ]),
    Q("en_library", ["apothic_enchanting:library", "apothic_enchanting:ender_library"], title="Library of Alexandria", x=20, y=2, deps=["en_draconic"], shape="gear", size=2.0, rew=["lv:60"], desc=[
        "Final: &eEnchantment Library&r büyülü kitapları içine atınca büyüleri saklar ve istediğin büyüyü istediğin seviyede bir kitaba geri çıkarır; aynı büyüden iki kitap atarak seviye yükseltebilirsin. Library'yi Eterna 100, Quanta 45-50, Arcana 100'de infuse edersen &eLibrary of Alexandria&r olur ve çok daha yüksek seviyeleri saklayabilir. Tebrikler, büyülemenin ustası oldun!",
    ]),
    Q("en_scrap", ["apothic_enchanting:scrap_tome", "apothic_enchanting:extraction_tome"], title="Büyüleri Kurtarmak", x=12, y=4, deps=["en_infuse"], optional=True, rew=["lv:15"], desc=[
        "Eski bir eşyanın büyüsünü kaybetmek istemiyor musun? &eTome of Scrapping&r'ı örste bir eşyayla birleştirirsen eşya kırılır, büyülerinin bir kısmı kitaba geçer. Eterna 45'te infuse edersen &eTome of Superior Scrapping&r (bütün büyüler), Eterna 60'ta infuse edersen &eTome of Extraction&r olur: eşyayı kırmadan bütün büyüleri kitaba çıkarır.",
    ]),
    Q("en_trident", ["apothic_enchanting:inert_trident", "minecraft:trident"], title="Trident Yapmak", x=6, y=4, deps=["en_hell_sea"], optional=True, desc=[
        "Drowned avlamaktan sıkıldın mı? Nautilus kabukları, Heart of the Sea ve demirle bir &eInert Trident&r yap, sonra Eterna 40, Quanta 20-50, Arcana 35'te infuse et: gerçek bir &eTrident&r.",
    ]),
])

artifacts = Chapter("artifacts", "Artifacts", "artifacts:cloud_in_a_bottle", "adventure", sub="Gizli hazineler ve aksesuarlar", quests=[
    Q("ar_intro", "check", title="Eserler ve Aksesuar Yuvaları", shape="hexagon", size=1.5, desc=[
        "&eArtifacts&r, zindan sandıklarında ve mağaralarda bulunan büyülü eserler ekler. Bunlar &eaksesuar yuvalarına&r takılır: envanterini açınca karakterinin yanında ekstra yuvalar (kafa, kolye, kemer, eldiven, ayakkabı...) görürsün. Her eser pasif bir güç verir: çift zıplama, hızlı koşma, su altında nefes, gece görüşü gibi. Çoğu üretilemez, sadece bulunur!",
    ]),
    Q("ar_mimic", "kill:artifacts:mimic", title="Mimic Avı", deps=["ar_intro"], rew=["xp:300"], desc=[
        "Dikkat: bazı sandıklar aslında &eMimic&r! Açmaya çalıştığında dişlerini gösterip sana saldırır. Mimic'ler yenildiğinde neredeyse her zaman bir eser düşürür, yani aslında iyi bir haber. Mağaralarda ve zindanlarda tek başına duran sandıklara şüpheyle yaklaş ve bir tane yen.",
    ]),
    Q("ar_cloud", "artifacts:cloud_in_a_bottle", deps=["ar_intro"], optional=True, desc=[
        "&eCloud in a Bottle&r havadayken bir kez daha zıplamanı sağlar (çift zıplama). Keşif ve dövüş için oyunun en sevilen eserlerinden.",
    ]),
    Q("ar_shoes", "artifacts:running_shoes", deps=["ar_intro"], optional=True, desc=[
        "&eRunning Shoes&r koşarken hızını artırır ve tek bloklara otomatik çıkmanı sağlar. Uzun yolculuklarda çok fark yaratır.",
    ]),
    Q("ar_glove", "artifacts:power_glove", deps=["ar_intro"], optional=True, desc=[
        "&ePower Glove&r yakın dövüş hasarını artırır. Better Combat'taki büyük silahlarla birlikte çok etkili.",
    ]),
    Q("ar_goggles", "artifacts:night_vision_goggles", deps=["ar_intro"], optional=True, desc=[
        "&eNight Vision Goggles&r karanlıkta görmeni sağlar; meşale koymadan mağara gezmek için birebir.",
    ]),
    Q("ar_heart", "artifacts:crystal_heart", deps=["ar_intro"], optional=True, desc=[
        "&eCrystal Heart&r maksimum canını artırır. Boss savaşlarından önce takmak isteyeceğin bir eser.",
    ]),
])

combat = Chapter("silahlar", "Silahlar ve Dövüş", "simplyswords:iron_longsword", "adventure", sub="Better Combat ve Simply Swords", quests=[
    Q("cb_combat", "check", title="Better Combat", shape="hexagon", size=1.5, desc=[
        "&eBetter Combat&r ile dövüş artık tıkla-vur değil. Her silahın kendine özgü bir &esaldırı animasyonu ve menzili&r var; ardı ardına vurunca &ekombo&r yaparsın (her vuruş bir öncekinden farklı). Kılıç geniş yay çizer ve birden çok düşmana vurabilir, mızrak uzaktan dürter, balta ağır ama sert vurur. Sol tık basılı tutarak sürekli saldırabilirsin. İki elde silah da taşıyabilirsin.",
    ]),
    Q("cb_longsword", "simplyswords:iron_longsword", deps=["cb_combat"], desc=[
        "&eSimply Swords&r onlarca yeni silah türü ekler: Longsword, Katana, Rapier, Greataxe, Glaive, Spear, Scythe, Claymore, Sai, Twinblade ve fazlası. Her biri farklı hız, menzil ve kombo sunar. Demir bir &eLongsword&r ile başla; dengeli ve kullanımı kolay.",
    ]),
    Q("cb_types", ["simplyswords:iron_katana", "simplyswords:iron_greataxe", "simplyswords:iron_spear"], title="Tarzını Bul", deps=["cb_longsword"], rew=["xp:200"], desc=[
        "Farklı silahları dene ve sana uyanı bul. &eKatana&r hızlı ve akıcı, &eGreataxe&r yavaş ama çok sert, &eSpear&r ise uzaktan vurmanı sağlar. Silahlar demir, altın, elmas ve netherite seviyelerinde gelir. Apotheosis bonuslarıyla birleştiğinde gerçekten güçlü olurlar.",
    ]),
    Q("cb_unique", "check", title="Eşsiz Silahlar", deps=["cb_types"], optional=True, rew=["xp:300"], desc=[
        "Simply Swords'un en değerli kısmı &eeşsiz (unique) silahlar&r: zindan sandıklarında bulunan, özel yetenekleri olan efsanevi silahlar (yıldırım çağıran, can çalan, ateş saçan...). Bazılarına &eRunefused&r ya da &eNetherfused&r gem takarak yeni güçler ekleyebilirsin. Bir eşsiz silah bulduğunda bu görevi işaretle.",
    ]),
])

bosses = Chapter("boss_avi", "Boss Avı", "minecraft:wither_skeleton_skull", "adventure", sub="Takımını topla!", shape="gear", quests=[
    Q("bs_intro", "check", title="Boss Avına Hazırlık", shape="hexagon", size=1.5, x=0, y=0, desc=[
        "Bu pakette vanilla'nın ötesinde birçok boss var; çoğu &eözel yapılarda&r bekliyor ve hepsi ciddi tehlike. Yalnız gitme, iyi zırh ve yemek al, iksir hazırla. Yerlerini bulmak için &eExplorer's Compass&r kullan. Ölürsen eşyaların mezar taşında kalır, ama yine de dikkatli ol. Her boss güzel ödüller ve büyük XP veriyor.",
    ]),
    Q("bs_wroughtnaut", "kill:mowziesmobs:ferrous_wroughtnaut", title="Ferrous Wroughtnaut", x=2, y=-3, deps=["bs_intro"], rew=["xp:500"], desc=[
        "Mowzie's Mobs'un ilk boss'u: yer altındaki bir odada uyuyan dev, zırhlı bir şövalye. Saldırılarından sonra kısa bir süre savunmasız kalır, &esırtına&r vurmak en etkilisi. Yendiğinde güçlü bir balta düşürür.",
    ]),
    Q("bs_frostmaw", "kill:mowziesmobs:frostmaw", title="Frostmaw", x=4, y=-3, deps=["bs_wroughtnaut"], rew=["xp:700"], desc=[
        "Karlı biyomlarda uyuyan dev bir buz canavarı. Buz nefesi ve yere vuruşlarıyla saldırır; ateş direnci yerine &esoğuğa karşı&r hazırlıklı ol. Yendiğinde bir &eIce Crystal&r düşürür, buz büyüsü yapan güçlü bir eşya.",
    ]),
    Q("bs_umvuthi", "kill:mowziesmobs:umvuthi", title="Umvuthi", x=6, y=-3, deps=["bs_frostmaw"], rew=["xp:800"], desc=[
        "Savan biyomlarındaki köylerin lideri, güneşin efendisi. Önce maskeli savaşçılarını yenmen gerekiyor, sonra kendisi güneş ışınlarıyla saldırır. Yendiğinde güneş gücünü kullandıran bir eşya bırakır.",
    ]),
    Q("bs_elder", "kill:minecraft:elder_guardian", title="Elder Guardian", x=2, y=0, deps=["bs_intro"], rew=["xp:400"], desc=[
        "Okyanus anıtlarının (Ocean Monument) bekçisi. YUNG's ile anıtlar daha büyük ve karmaşık. Su altında kazma hızını düşüren laneti var; Conduit ya da su altı iksirleriyle git.",
    ]),
    Q("bs_wither", "kill:minecraft:wither", title="Wither", x=4, y=0, deps=["bs_elder"], rew=["xp:800"], desc=[
        "3 Wither Skeleton kafası ve 4 Soul Sand ile çağrılan klasik boss. Patlamaları çevreyi yok eder, o yüzden üssünden uzakta çağır. Yendiğinde düşen &eNether Star&r birçok ileri seviye tarifte lazım (Powah Nitro, Apotheosis Augmenting Table...).",
    ]),
    Q("bs_warden", "kill:minecraft:warden", title="Warden", x=6, y=0, deps=["bs_wither"], rew=["xp:1000"], desc=[
        "Ancient City'lerin kör bekçisi; sesleri duyar ve çok sert vurur. Normalde kaçmak önerilir ama Apothic Enchanting'in &eWarden Tendril&r'ı için onu yenmen gerekiyor. Takımca gidin, uzaktan saldırın ve sessiz olun.",
    ]),
    Q("bs_ender_guardian", "kill:cataclysm:ender_guardian", title="Ender Guardian", x=2, y=3, deps=["bs_intro"], rew=["xp:1000"], desc=[
        "&eL_Ender's Cataclysm&r boss'ları paketin en zorlu düşmanları. &eEnder Guardian&r End'deki &eRuined Citadel&r'da bekler: ışınlanır, yerçekimiyle oynar ve dev yumruklarla vurur. Cataclysm boss'larının her biri benzersiz silah ve malzemeler düşürür.",
    ]),
    Q("bs_monstrosity", "kill:cataclysm:netherite_monstrosity", title="Netherite Monstrosity", x=4, y=3, deps=["bs_ender_guardian"], rew=["xp:1000"], desc=[
        "Nether'deki &eSoul Black Smith&r yapısında yatan dev bir netherit golem. Lav topları fırlatır ve yeri sarsar. Ateş direnci iksiri olmadan gitme!",
    ]),
    Q("bs_ignis", "kill:cataclysm:ignis", title="Ignis", x=6, y=3, deps=["bs_monstrosity"], rew=["xp:1200"], desc=[
        "Nether'deki &eBurning Arena&r'nın alevli şövalyesi. Kalkanını kırman, sonra hızlı saldırılarından kaçman gerekiyor. Ateş direnci ve iyi bir kalkan şart.",
    ]),
    Q("bs_harbinger", "kill:cataclysm:the_harbinger", title="The Harbinger", x=8, y=3, deps=["bs_ignis"], rew=["xp:1200"], desc=[
        "Yer altındaki &eAncient Factory&r'de bekleyen dev bir savaş makinesi; lazerler ve füzelerle saldırır. Wither'dan bile tehlikeli, takımca gidin.",
    ]),
    Q("bs_leviathan", "kill:cataclysm:the_leviathan", title="The Leviathan", x=8, y=1, deps=["bs_harbinger"], rew=["xp:1500"], desc=[
        "Derin okyanusun altındaki &eSunken City&r'nin efendisi, devasa bir deniz canavarı. Su altında savaşacağın için su altı nefesi ve hızlı yüzme şart.",
    ]),
    Q("bs_remnant", "kill:cataclysm:ancient_remnant", title="Ancient Remnant", x=8, y=5, deps=["bs_harbinger"], rew=["xp:1500"], desc=[
        "Çöldeki &eCursed Pyramid&r'in derinliklerinde uyuyan kadim bir firavun iskeleti. Kum fırtınaları ve dev kemik saldırılarıyla savaşır.",
    ]),
    Q("bs_maledictus", "kill:cataclysm:maledictus", title="Maledictus", x=10, y=3, deps=["bs_leviathan", "bs_remnant"], shape="gear", size=1.5, rew=["xp:2000"], desc=[
        "Karlı dağlardaki &eFrosted Prison&r'da hapsedilmiş lanetli bir ruh. Cataclysm'in en zor boss'larından biri. Onu da yendiysen bu sunucunun efsanesi sizsiniz!",
    ]),
])

ADVENTURE = [explore, apo, artifacts, combat, bosses]
