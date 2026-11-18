from engine import Chapter, Q

soph = Chapter("sophisticated_storage", "Sophisticated Storage", "sophisticatedstorage:gold_chest", "storage", sub="Büyüyen sandıklar ve varil", quests=[
    Q("ss_chest", ["sophisticatedstorage:chest", "sophisticatedstorage:barrel"], title="Chest ve Barrel", shape="hexagon", size=1.5, rew=["xp:100"], desc=[
        "&eSophisticated Storage&r normal sandıkların süper güçlü hali. &eChest&r ve &eBarrel&r ilk bakışta vanilla sandık gibi, ama yükseltilebilir ve içlerine upgrade takılabilir. Ahşap türüne göre görünüşleri değişir, yerleştirdikten sonra boyayla (Paintbrush) renklendirebilirsin bile. Üssündeki bütün sandıkları bunlarla değiştirmek isteyeceksin.",
    ]),
    Q("ss_tier_iron", "sophisticatedstorage:basic_to_iron_tier_upgrade", title="Seviye Yükseltme", deps=["ss_chest"], desc=[
        "Sandığı kırıp yeniden yapmana gerek yok: elinde &eBasic to Iron Tier Upgrade&r varken yerleştirdiğin sandığa ya da varile sağ tıkla, içindekiler kaybolmadan &eIron&r seviyeye yükselir. Her seviye (Copper → Iron → Gold → Diamond → Netherite) daha fazla yuva ve daha fazla upgrade yeri verir. Netherite seviye sandıklar patlamaya bile dayanıklı.",
    ]),
    Q("ss_tier_diamond", "sophisticatedstorage:diamond_chest", title="Diamond Chest", deps=["ss_tier_iron"], desc=[
        "Yükseltmeye devam et: altın, sonra elmas. &eDiamond Chest&r normal bir sandığın yaklaşık 4 katı alan sunar ve 4 upgrade yuvası vardır. Büyük madenciliklerden sonra her şeyi koyacak yerin olur.",
    ]),
    Q("ss_upgrades", ["sophisticatedstorage:compacting_upgrade", "sophisticatedstorage:void_upgrade"], title="Compacting ve Void", deps=["ss_tier_iron"], rew=["xp:150"], desc=[
        "Upgrade'ler sandığın menüsündeki sağ yuvalara takılır. &eCompacting Upgrade&r içine giren eşyaları otomatik sıkıştırır: 9 demir külçe → 1 demir bloğu, böylece 9 kat yer kazanırsın. &eVoid Upgrade&r istemediğin eşyaları (çakıl, toprak, andezit fazlası) silip yok eder; içine filtre olarak koyduğun eşyalar sandığa girer girmez kaybolur. Madenden gelen çöpler için çok kullanışlı.",
    ]),
    Q("ss_hopper", ["sophisticatedstorage:hopper_upgrade", "sophisticatedstorage:smelting_upgrade"], title="Hopper ve Smelting", deps=["ss_upgrades"], desc=[
        "&eHopper Upgrade&r sandığın yanındaki sandıklardan eşya çeker ya da onlara eşya iter, filtreli bir huni gibi. &eSmelting Upgrade&r ise sandığa küçük bir fırın ekler: içine koyduğun cevherleri kendi içinde eritir. Upgrade'lerin 'Advanced' sürümleri daha fazla filtre ve ayar sunar.",
    ]),
    Q("ss_limited", "sophisticatedstorage:limited_barrel_1", title="Limited Barrel", deps=["ss_chest"], optional=True, desc=[
        "&eLimited Barrel&r her bölmesinde tek tür eşyadan çok büyük miktarlar tutar; ön yüzünde neyin ne kadar olduğunu görürsün. Ön yüzüne sağ tıklayarak eşya koyar, sol tıklayarak alırsın. Taş, toprak, odun gibi bol bulunan eşyalar için idealdir. 1, 2, 3 ve 4 bölmeli türleri var.",
    ]),
    Q("ss_controller", ["sophisticatedstorage:controller", "sophisticatedstorage:oak_storage_connector*4"], title="Controller: Birleşik Depo", deps=["ss_upgrades"], shape="gear", size=1.5, rew=["xp:300"], desc=[
        "&eStorage Controller&r birbirine değen bütün Sophisticated sandık ve varilleri tek bir depo gibi birleştirir. Uzaktaki sandıkları &eStorage Connector&r bloklarıyla bağlayabilirsin. Controller'a sağ tıklayıp elindeki eşyaları atarsan, eşyalar zaten o eşyayı içeren sandığa otomatik dağılır. Borularla Controller'a eşya gönderirsen hepsi düzenli şekilde yerine gider. Dağınık üslerin kurtarıcısı!",
    ]),
])

rs = Chapter("refined_storage", "Refined Storage", "refinedstorage:controller", "storage", sub="Dijital depolama ağı ve otomatik üretim", quests=[
    Q("rs_silicon", ["refinedstorage:silicon*4", "refinedstorage:quartz_enriched_iron*8"], title="Silicon ve Quartz Enriched Iron", shape="hexagon", size=1.5, desc=[
        "&eRefined Storage&r eşyalarını sandık yerine &edisklere&r kaydeden dijital bir depolama sistemi. Bütün eşyaların tek bir ekranda, aranabilir halde durur. Başlamak için iki malzeme lazım: Nether Quartz'ı fırında eriterek &eSilicon&r, demir ve kuvarsı birleştirerek &eQuartz Enriched Iron&r yaparsın.",
    ]),
    Q("rs_processor", ["refinedstorage:basic_processor*4", "refinedstorage:machine_casing*2"], title="Processor ve Machine Casing", deps=["rs_silicon"], desc=[
        "Önce ip ve slime topuyla &eProcessor Binding&r yap. Sonra bunu demir, Silicon ve kızıltaş ile birleştirip ham işlemci (&eRaw Basic Processor&r) yap ve fırında pişir: &eBasic Processor&r. Demir yerine altın kullanırsan &eImproved&r, elmas kullanırsan &eAdvanced Processor&r olur. &eMachine Casing&r ise RS bloklarının gövdesi.",
    ]),
    Q("rs_controller", "refinedstorage:controller", deps=["rs_processor"], rew=["xp:150"], desc=[
        "&eController&r ağın beyni. Ağdaki her şey ona kablo (&eCable&r) ya da doğrudan temasla bağlanmalı. Controller &eelektrikle&r çalışır, yani yanına bir jeneratör ya da güç kablosu bağlaman gerekir (Powah, Mekanism, Pipez vb.). Ağa ne kadar çok cihaz bağlarsan o kadar enerji harcar. Ağda tek bir Controller olmalı.",
    ]),
    Q("rs_disk", ["refinedstorage:disk_drive", "refinedstorage:1k_storage_disk*2"], title="Disk Drive ve Storage Disk", deps=["rs_controller"], desc=[
        "Eşyalar &eStorage Disk&r'lerde saklanır. &e1k Storage Disk&r 1000 eşya tutar (eşyanın türü fark etmez). Diskleri ağa bağlı bir &eDisk Drive&r'a takarsın; bir Disk Drive 8 disk alır. Daha sonra 4k, 16k ve 64k diskler yaparak kapasiteyi kat kat artırabilirsin. Diskin içindeki eşyalar disk sökülse bile kaybolmaz.",
    ]),
    Q("rs_grid", ["refinedstorage:grid", "refinedstorage:crafting_grid"], title="Grid", deps=["rs_disk"], rew=["xp:150"], desc=[
        "&eGrid&r ağdaki bütün eşyaları gösteren ekran. Eşya koyar, alır ve arama kutusundan istediğini anında bulursun. &eCrafting Grid&r'da bir de çalışma masası vardır ve tariflerin malzemelerini doğrudan ağdan çeker. JEI'den bir tarifi seçip '+' tuşuna basarsan malzemeler otomatik yerleşir.",
    ]),
    Q("rs_external", "refinedstorage:external_storage", deps=["rs_grid"], desc=[
        "Var olan sandıklarını da ağa eklemek ister misin? &eExternal Storage&r'ı bir sandığa (ya da Sophisticated sandığa, varile...) bakacak şekilde ağa bağla; o sandığın içeriği Grid'de görünür ve ağın bir parçası olur. Diskler dolduğunda büyük sandıklarını bu şekilde depolama olarak kullanabilirsin.",
    ]),
    Q("rs_io", ["refinedstorage:importer", "refinedstorage:exporter"], title="Importer ve Exporter", deps=["rs_grid"], desc=[
        "&eImporter&r baktığı bloktan (fırın, makine, sandık) eşyaları çekip ağa alır, &eExporter&r ise ağdan eşyaları baktığı bloğa gönderir. Filtre yuvalarına hangi eşyaları taşıyacaklarını koyarsın. Örneğin bir fırına Exporter ile cevher gönderip altındaki Importer ile külçeleri geri alarak otomatik bir eritme sistemi kurabilirsin.",
    ]),
    Q("rs_autocraft", ["refinedstorage:pattern_grid", "refinedstorage:autocrafter", "refinedstorage:pattern*8"], title="Otomatik Üretim", deps=["rs_io"], shape="gear", size=1.5, rew=["xp:300"], desc=[
        "Refined Storage'ın en güçlü özelliği. &ePattern Grid&r'da bir tarifi boş bir &ePattern&r'e kaydedersin, sonra bu pattern'ı ağa bağlı bir &eAutocrafter&r'a takarsın. Artık Grid'de o eşyaya tıkladığında 'kaç tane yapılsın' diye sorar ve ağ malzemeleri kendisi toplayıp üretir. Makine tarifleri için de 'processing' pattern'ları ile Autocrafter'ı makinelerin yanına koyabilirsin. Alt tarifler de otomatik çözülür!",
    ]),
    Q("rs_wireless", ["refinedstorage:wireless_grid", "refinedstorage:wireless_transmitter"], title="Kablosuz Grid", deps=["rs_grid"], rew=["xp:200"], desc=[
        "&eWireless Transmitter&r'ı ağa bağla, sonra &eWireless Grid&r ile ağdaki herhangi bir cihaza (örneğin Controller'a) sağ tıklayarak onu ağına bağla. Artık vericinin menzilindeyken cebinden bütün deponu açabilirsin. Upgrade'lerle menzil artırılabilir. Wireless Grid elektrik harcar, arada şarj etmen gerekir.",
    ]),
])

STORAGE = [soph, rs]
