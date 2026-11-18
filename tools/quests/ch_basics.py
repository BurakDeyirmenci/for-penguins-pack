from engine import Chapter, Q

basics = Chapter("temeller", "Temeller", "minecraft:blue_ice", None, sub="Buradan başla!", quests=[
    Q("welcome", "check", title="&bFor Penguins'e Hoş Geldin!", shape="hexagon", size=2.0, x=0, y=0, rew=["xp:100", "minecraft:cooked_cod*16"], desc=[
        "Bu paket arkadaşlarla birlikte oynamak için hazırlanmış bir mod paketi. Teknoloji, büyü, depolama ve macera modları var ve bu görev kitabı her birini adım adım öğretiyor.",
        "",
        "Önce buradaki kısa görevleri oku, sonra soldaki sekmelerden ilgini çeken modu seç. Görevlerde geçen eşya adları oyunda göründüğü gibi İngilizce yazıldı, böylece JEI'de aradığında aynısını bulursun.",
        "",
        "&bUnutma Her Şey Penguenler İçin 😉",
    ]),
    Q("map", "check", title="Harita ve Waypoint", sub="FTB Chunks", deps=["welcome"], x=-3, y=-2.5, desc=[
        "Sağ üstteki küçük harita (minimap) FTB Chunks moduna ait. &eM&r tuşuna basınca büyük harita açılır; gezdiğin her yer burada kayıtlı kalır, yani kaybolmak neredeyse imkansız. Büyük haritada bir yere sağ tıklayıp waypoint (işaret noktası) ekleyebilirsin: evini, bir köyü ya da güzel bir mağarayı işaretle, ekranda yönü ve uzaklığı görünür. Öldüğünde de ölüm yerine otomatik bir işaret konur, eşyalarını kolayca bulursun.",
    ]),
    Q("claim", "check", title="Chunk Sahiplenme", sub="FTB Chunks", deps=["map"], x=-4.5, y=-4, desc=[
        "Dünya 16x16 blokluk parçalara bölünmüştür, bunlara &echunk&r denir. Büyük haritayı açıp (&eM&r) sol üstteki chunk ekranına girersen etrafındaki chunk'ları görürsün; sol tıklayıp sürükleyerek sahiplenir, sağ tıklayıp sürükleyerek bırakırsın. Sahiplendiğin yerde senin (ve takım arkadaşlarının) dışında kimse blok kıramaz, sandık açamaz, patlamalar da hasar vermez. Shift basılıyken tıklarsan chunk'ı &eforce load&r yaparsın: sen uzaktayken bile oradaki makineler çalışmaya devam eder. Makine kurduğun alanlar için çok önemli!",
    ]),
    Q("team", "check", title="Takım Kur", sub="FTB Teams", deps=["welcome"], x=-3, y=0, desc=[
        "Arkadaşlarınla aynı takımda olursanız görev ilerlemesi, sahiplenilen chunk'lar ve bazı mod verileri ortak olur. Envanterini açınca sol üstte küçük simgeler görürsün; takım simgesine tıkla, &eCreate Party&r ile bir takım oluştur ve arkadaşlarını davet et. Davet gelen kişi aynı menüden kabul eder. Takımdayken bir kişinin bitirdiği görev herkes için biter ve herkes ödülünü kendisi alır, o yüzden işi bölüşmek çok kolaylaşır.",
    ]),
    Q("jei", "check", title="JEI: Tarif Kitabın", sub="Just Enough Items", deps=["welcome"], x=-3, y=2.5, desc=[
        "Envanterini açınca sağ tarafta paketteki bütün eşyaların listesi çıkar; bu &eJEI&r. Bir eşyanın üzerine gelip &eR&r'ye basarsan nasıl yapıldığını, &eU&r'ya basarsan nerelerde kullanıldığını gösterir. Makinelerin tarifleri de burada: ne yapacağını bilmediğinde ilk bakacağın yer burası. Alttaki arama kutusuna isim yazarak arayabilir, &eA&r ile eşyaları yer imlerine ekleyebilirsin. Ayrıca ekranın üstünde baktığın bloğun adını ve hangi moda ait olduğunu gösteren küçük bir kutu var (Jade); bir şeyin hangi moddan geldiğini merak edersen ona bak.",
    ]),
    Q("ultimine", "check", title="Ultimine: Toplu Kazma", sub="FTB Ultimine", deps=["welcome"], x=-4.5, y=4, desc=[
        "Normalde her bloğu tek tek kırarsın, ama bu pakette &e`&r (Esc'in altındaki) tuşunu basılı tutarak birbirine bağlı aynı blokları tek seferde kazabilirsin. Bir demir damarına bakıp tuşu basılı tutarsan hangi blokların kırılacağı beyaz çizgiyle gösterilir, sonra normal şekilde kazman yeterli. Ağaç kesmek, taş düzlemek ya da cevher damarlarını toplamak için çok işine yarar. Her blok biraz açlık harcar, yanında yemek bulunsun!",
    ]),
    Q("voice", "check", title="Sesli Sohbet", sub="Simple Voice Chat", deps=["welcome"], x=3, y=-2.5, desc=[
        "Oyunun içinde konuşabilirsiniz! Ses yakınlığa göre çalışır: yanındaki oyuncular seni duyar, uzaklaştıkça sesin kısılır. &eV&r tuşu ayarları açar; buradan mikrofonunu seçip sesini test edebilirsin. Varsayılan olarak bas-konuş açıktır, &eCaps Lock&r'a basılı tutarken konuşursun; istersen ayarlardan sesle otomatik açılma moduna geçebilirsin. Menüden bir grup kurarsan uzakta olsanız bile grup içindekiler birbirini duyar.",
    ]),
    Q("carryon", "check", title="Carry On: Taşıma", sub="Carry On", deps=["welcome"], x=3, y=0, desc=[
        "Elin boşken &eShift + sağ tık&r yaparsan sandıkları içindekilerle birlikte, hatta hayvanları kucağına alıp taşıyabilirsin. Yere bırakmak için istediğin yere tekrar sağ tıkla. Evi taşırken sandıkları boşaltmana gerek kalmaz, koyunları ağıla da tek tek ip ile götürmezsin. Taşırken yavaş yürürsün ve başka bir şey tutamazsın, o yüzden tehlikeli yerlerde dikkat et.",
    ]),
    Q("grave", "check", title="Mezar Taşı", sub="Gravestone", deps=["welcome"], x=3, y=2.5, desc=[
        "Öldüğünde eşyaların yere saçılıp kaybolmaz; öldüğün yerde bir mezar taşı çıkar ve bütün eşyaların onun içinde saklanır. Geri dönüp mezar taşını kırdığında ya da ona sağ tıkladığında eşyaların geri gelir. Haritada ölüm yerin işaretli olduğu için bulmak kolaydır. Lavda ya da boşlukta ölürsen mezar taşı en yakın güvenli yere konur, yine de lavla oynamamak en iyisi.",
    ]),
    Q("backpack", "sophisticatedbackpacks:backpack", sub="Sophisticated Backpacks", deps=["welcome"], x=0, y=3, rew=["xp:100"], desc=[
        "Sırt çantası, yanında taşıyabileceğin ikinci bir envanter. Deri, sandık ve ip ile yapılır (tarif için JEI'ye bak). Çanta envanterindeyken &eB&r tuşuyla açılır; Shift + sağ tık ile yere de koyabilirsin. Çantanın yan tarafındaki yuvalara &eupgrade&r takarak ona yeni özellikler kazandırabilirsin, bunları sonraki görevlerde göreceğiz.",
    ]),
    Q("backpack_iron", "sophisticatedbackpacks:iron_backpack", deps=["backpack"], x=0, y=4.5, rew=["xp:150"], desc=[
        "Çantayı ortaya koyup etrafını demir külçeyle doldurursan içindekiler kaybolmadan &eIron Backpack&r'e yükselir: daha fazla yuva ve daha fazla upgrade yeri. Aynı şekilde altın, elmas ve netherite ile de yükseltmeye devam edebilirsin. Her seviye hem alanı hem upgrade yuvası sayısını artırır.",
    ]),
    Q("backpack_pickup", "sophisticatedbackpacks:pickup_upgrade", deps=["backpack_iron"], x=0, y=6, rew=["xp:150"], desc=[
        "Upgrade'lerin hepsi &eUpgrade Base&r ile başlar. &ePickup Upgrade&r takılı çanta, yerden topladığın eşyaları otomatik olarak çantaya koyar; içine filtre koyarak sadece istediğin eşyaları (örneğin cevherleri) toplamasını sağlayabilirsin. Upgrade'i takmak için çantayı aç ve sağdaki yuvalara sürükle. Magnet, Feeding (acıkınca seni besler), Crafting gibi başka upgrade'lere de JEI'den göz at.",
    ]),
    Q("waystone", "check", title="Waystone Bul", sub="Waystones", deps=["welcome"], x=0, y=-3, desc=[
        "Köylerde ve dünyanın çeşitli yerlerinde üstü parlayan taş sütunlar göreceksin, bunlar &eWaystone&r. Birine sağ tıklarsan onu etkinleştirirsin ve listene eklenir. Sonra herhangi bir waystone'a sağ tıklayıp listeden daha önce etkinleştirdiğin başka bir waystone'a ışınlanabilirsin. Işınlanmak biraz XP harcar, mesafe uzadıkça bedel artar. Kendi üssüne de bir waystone koyarsan her yerden eve dönmek çok kolaylaşır.",
    ]),
    Q("warp_scroll", "waystones:warp_scroll", deps=["waystone"], x=0, y=-4.5, rew=["xp:100", "waystones:warp_scroll*2"], desc=[
        "&eWarp Scroll&r tek kullanımlık bir ışınlanma parşömeni: kullandığında waystone listen açılır ve bir waystone'un başında olmasan bile istediğine gidebilirsin. Uzak bir maceradayken eve dönmek için cebinde bir tane bulunsun. &eReturn Scroll&r ise seni en son kullandığın waystone'a geri götürür.",
    ]),
    Q("tiab", "tiab:time_in_a_bottle", sub="Time in a Bottle", deps=["welcome"], x=4.5, y=-4, rew=["xp:300"], desc=[
        "Bu şişe envanterinde dururken &ezaman biriktirir&r. Biriken zamanı bir makineye, fırına, fidana ya da ekine sağ tıklayarak harcarsın ve o şey birkaç kat hızlı çalışır. Her tıklama hızı ikiye katlar ama daha çok zaman harcar. Yavaş büyüyen ağaçlar, uzun süren makine işleri ya da fırında bekleyen cevherler için birebir. Yapımı için altın, elmas, saat ve lapis gerekiyor, JEI'den tarifine bak.",
    ]),
    Q("choose", "check", title="Yolunu Seç", shape="gear", size=1.5, deps=["team", "jei"], x=7, y=0, rew=["xp:200"], desc=[
        "Temelleri öğrendin! Artık soldaki sekmelerden istediğin yolu seçebilirsin:",
        "",
        "&6Teknoloji&r: Create, Mekanism, Powah ve diğerleriyle makineler, enerji ve otomasyon.",
        "&9Depolama&r: Binlerce eşyayı düzenli tutan sandıklar ve dijital depolama ağları.",
        "&dBüyü&r: Ars Nouveau, Botania, Iron's Spells ve Occultism ile büyüler ve ritüeller.",
        "&cMacera&r: Keşif, Apotheosis ekipmanı ve büyüleri, eserler, silahlar ve boss'lar.",
        "",
        "Hepsini aynı anda oynamak zorunda değilsin; takımca işi bölüşmek çok daha eğlenceli.",
    ]),
])
