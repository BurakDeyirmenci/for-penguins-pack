from engine import Chapter, Q

ars = Chapter("ars_nouveau", "Ars Nouveau", "ars_nouveau:novice_spell_book", "magic", sub="Kendi büyülerini tasarla", quests=[
    Q("ars_notebook", "ars_nouveau:worn_notebook", shape="hexagon", size=1.5, desc=[
        "&eArs Nouveau&r'da büyüleri kendin tasarlarsın: bir 'şekil' (kendine, vurduğun yere, fırlatılan bir top...) ve 'etkiler' (hasar, kazma, iyileştirme...) seçip birleştirirsin. Önce bir kitap ve lapis ile &eWorn Notebook&r yap; bu modun kılavuzu, her şeyin nasıl yapıldığını anlatır. Bir sonraki adım için Archwood ağaçlarını (renkli yapraklı büyülü ağaçlar) bulmaya başla.",
    ]),
    Q("ars_book", "ars_nouveau:novice_spell_book", deps=["ars_notebook"], rew=["xp:150"], desc=[
        "&eNovice Spell Book&r ilk büyü kitabın: kitap (ya da Worn Notebook) ile demir kürek, kazma, balta ve kılıcı birleştirerek yaparsın. Kitabı elindeyken &eC&r tuşuna basarak büyü düzenleyiciyi aç, ilk büyünü oluştur: örneğin &eProjectile + Harm&r (hasar veren bir top) ya da &eTouch + Break&r (dokunduğun bloğu kır). Büyüler 'mana' harcar, mana zamanla kendiliğinden dolar. Kitaptaki büyüler arasında geçiş tuşlarını Ayarlar > Kontroller > Tuşlar menüsündeki 'Ars Nouveau' bölümünde görebilirsin.",
    ]),
    Q("ars_gem", ["ars_nouveau:imbuement_chamber", "ars_nouveau:source_gem*4"], title="Source Gem", deps=["ars_book"], desc=[
        "&eSource&r, Ars Nouveau'nun büyülü enerjisi; &eSource Gem&r ise bu enerjinin katı hali. Archwood tahtası ve altınla bir &eImbuement Chamber&r yap, içine ametist kırığı ya da lapis koy. Yakında source yoksa çok yavaş çalışır; bir sonraki görevdeki Source Jar ile hızlanır. Source Gem neredeyse bütün Ars tariflerinde lazım.",
    ]),
    Q("ars_source", ["ars_nouveau:source_jar*2", "ars_nouveau:volcanic_sourcelink"], title="Source Jar ve Sourcelink", deps=["ars_gem"], rew=["xp:150"], desc=[
        "&eSource Jar&r source depolar; yakınındaki makineler kullanmak için ondan çeker. &eSourcelink&r'ler ise source üretir: &eVolcanic Sourcelink&r yakınında yanan yakıtlardan (odun, kömür, lav), &eAgronomic&r büyüyen bitkilerden, &eMycelial&r yenen yemeklerden, &eVitalic&r doğan ve ölen hayvanlardan source üretir. Sourcelink'i jar'ın yakınına koy, jar dolsun.",
    ]),
    Q("ars_scribe", "ars_nouveau:scribes_table", title="Scribe's Table ve Glyph'ler", deps=["ars_gem"], desc=[
        "Yeni büyü parçaları (&eGlyph&r) öğrenmek için &eScribe's Table&r lazım. Masaya sağ tıklayıp öğrenmek istediğin glyph'i seç; malzemeleri masaya koyduğunda boş bir glyph'i (Blank Glyph) o parçaya çevirir. Glyph'i kullandığında kitabına eklenir. Bazı güçlü glyph'ler ancak üst seviye büyü kitaplarında kullanılabilir.",
    ]),
    Q("ars_apparatus", ["ars_nouveau:enchanting_apparatus", "ars_nouveau:arcane_core"], title="Enchanting Apparatus", deps=["ars_source"], rew=["xp:200"], desc=[
        "&eEnchanting Apparatus&r, Ars'ın ileri tarif makinesi: &eArcane Core&r'un üstüne konur, etrafına &eArcane Pedestal&r'lar dizilir. Ortadaki eşyaya kaidelerdeki malzemeleri source harcayarak birleştirir. Büyü kitaplarını yükseltmek, büyülü yüzükler, eşyalara büyü eklemek ve zırhlar hep burada yapılır.",
    ]),
    Q("ars_apprentice", "ars_nouveau:apprentice_spell_book", deps=["ars_apparatus"], rew=["xp:250"], desc=[
        "&eApprentice Spell Book&r: Novice kitabını Enchanting Apparatus'ta obsidyen, elmas ve kuvars bloklarıyla yükselt. Daha fazla mana, daha fazla büyü yuvası ve orta seviye glyph'leri kullanma hakkı verir. Büyülerine artık &eAmplify&r (güçlendir), &eAOE&r (alan etkisi) gibi geliştirmeler ekleyebilirsin.",
    ]),
    Q("ars_archmage", "ars_nouveau:archmage_spell_book", deps=["ars_apprentice"], shape="gear", size=1.5, rew=["xp:400"], desc=[
        "&eArchmage Spell Book&r, en güçlü büyü kitabı: Apprentice kitabını ender incisi, zümrüt ve bir &eTotem of Undying&r gibi nadir malzemelerle yükseltirsin. Bütün glyph'leri kullanabilir ve en uzun büyü dizilerini yazabilirsin. Artık gerçek bir büyücüsün!",
    ]),
    Q("ars_familiar", "check", title="Familiar ve Ritüeller", deps=["ars_apparatus"], optional=True, desc=[
        "Ars Nouveau'da küçük yardımcı yaratıklar da var. &eStarbuncle&r eşya taşır, &eWixie&r iksir ve tarif yapar, &eWhirlisprig&r bitkileri büyütür, &eDrygmy&r yaratıklardan ganimet toplar. Bunları &eFamiliar&r olarak yanında da gezdirebilirsin, sana bonus verirler. &eRitual Brazier&r ile hava durumunu değiştiren, ekinleri büyüten ritüeller yapabilirsin. Kılavuzda (Worn Notebook) hepsinin sayfası var.",
    ]),
])

botania = Chapter("botania", "Botania", "botania:pure_daisy", "magic", sub="Çiçeklerle teknoloji", quests=[
    Q("bt_lexicon", "botania:lexicon", shape="hexagon", size=1.5, desc=[
        "&eBotania&r bir 'doğa büyüsü' modu: çiçekler &emana&r üretir, mana ile makineler ve büyülü eşyalar yapılır. Her şey dünyada rastgele çıkan renkli &eMystical Flower&r'larla başlar; bunları kırınca ya da üzerlerine kemik tozu atınca taç yaprak (petal) verirler. Bir kitap ve herhangi bir fidanla (sapling) &eLexica Botania&r kılavuzunu yap.",
    ]),
    Q("bt_apothecary", ["botania:apothecary_default", "botania:white_mystical_flower*4"], title="Petal Apothecary", deps=["bt_lexicon"], desc=[
        "&ePetal Apothecary&r özel çiçekler yaptığın kazandır. İçini su ile doldur (kovayla sağ tık), tarifin taç yapraklarını içine at, en son bir tohum (wheat seeds) at: yeni çiçek havaya fırlar. Her özel çiçeğin tarifini Lexicon'da ya da JEI'de görebilirsin. Taç yaprakları çoğaltmak için çiçeklerin üzerine kemik tozu at.",
    ]),
    Q("bt_daisy", ["botania:pure_daisy", "botania:livingrock*8", "botania:livingwood_log*8"], title="Pure Daisy", deps=["bt_apothecary"], rew=["xp:150"], desc=[
        "&ePure Daisy&r, 4 beyaz taç yaprakla yapılır ve Botania'nın ilk çiçeğidir. Yere dik, etrafındaki 8 bloğa taş ya da odun koy; bir süre sonra taşlar &eLivingrock&r'a, odunlar &eLivingwood&r'a dönüşür. Bu iki malzeme Botania'nın yapı taşları, bol bol yap.",
    ]),
    Q("bt_wand", "botania:twig_wand", deps=["bt_daisy"], desc=[
        "&eWand of the Forest&r Botania'nın aleti: Livingwood çubukları ve taç yapraklarla yapılır. Shift + sağ tık ile iki modu arasında geçiş yaparsın: &eBind&r modunda çiçekleri ve Spreader'ları birbirine bağlar, &eFunction&r modunda Spreader'ları döndürür ve makineleri çalıştırırsın. Bloklara baktığında içlerindeki mana miktarını da gösterir.",
    ]),
    Q("bt_mana", ["botania:mana_spreader", "botania:mana_pool"], title="Mana Spreader ve Mana Pool", deps=["bt_wand"], rew=["xp:200"], desc=[
        "Mana çiçeklerden &eMana Spreader&r'a, oradan da ışın halinde &eMana Pool&r'a gider. Spreader'ı Wand ile havuza bağla (Spreader'a sonra havuza tıkla), mana üreten çiçeği de Spreader'ın yakınına koy. İlk başta ucuz &eDiluted Mana Pool&r'u da kullanabilirsin. Havuzu Livingrock'tan yaparsın; içine baktığında ne kadar mana olduğunu görürsün.",
    ]),
    Q("bt_endoflame", "botania:endoflame*2", deps=["bt_mana"], desc=[
        "&eEndoflame&r ilk mana üreten çiçeğin: yakınındaki yere attığın yakıtları (kömür, odun) yakarak mana üretir. Birkaç tane yapıp yanlarına bir Spreader koy ve kömür ver. Gündüzleri güneşten mana üreten (Daybloom) ve sudan üreten (Hydroangeas) çiçekler de var; Lexicon'daki 'Generating Flora' bölümüne bak.",
    ]),
    Q("bt_manasteel", "botania:manasteel_ingot*8", deps=["bt_endoflame"], rew=["xp:200"], desc=[
        "Mana Pool'a bir demir külçe atarsan mana harcayarak &eManasteel Ingot&r'a dönüştürür. Havuza attığın birçok eşya bu şekilde dönüşür: elmas → Mana Diamond, ender incisi → Mana Pearl, ip → Mana String. Manasteel aletleri mana ile kendini tamir eder.",
    ]),
    Q("bt_runes", ["botania:runic_altar", "botania:rune_water", "botania:rune_fire", "botania:rune_earth", "botania:rune_air"], title="Runic Altar ve Rünler", deps=["bt_manasteel"], desc=[
        "&eRunic Altar&r, Botania'nın tarif masası. Mana Spreader ile manayı altara gönder, malzemeleri içine at, son olarak bir &eLivingrock&r koy ve Wand ile vur. Dört temel rün (Su, Ateş, Toprak, Hava) birçok ileri tarifte lazım. Mevsim ve günah rünleri de bu dört rünle yapılır.",
    ]),
    Q("bt_terrasteel", ["botania:terra_plate", "botania:terrasteel_ingot"], title="Terrasteel", deps=["bt_runes"], shape="gear", size=1.5, rew=["xp:400"], desc=[
        "&eTerrestrial Agglomeration Plate&r'ı özel bir kare taban üzerine (Lapis ve Livingrock deseni, Lexicon'da gösteriliyor) kur. Üzerine Manasteel Ingot, Mana Pearl ve Mana Diamond at ve Spreader'larla büyük miktarda mana gönder: &eTerrasteel Ingot&r çıkar. Bu Botania'nın orta seviyesinin zirvesi; Terrasteel aletleri ve zırhı çok güçlü.",
    ]),
    Q("bt_alfheim", "botania:alfheim_portal", title="Alfheim Portalı", deps=["bt_terrasteel"], rew=["xp:300"], desc=[
        "Elf diyarı &eAlfheim&r'e açılan bir kapı! &eElven Gateway Core&r'u Livingwood ve Glimmering Livingwood ile kurulan bir çerçeveye yerleştir, yanına Natura Pylon'lu Mana Pool'lar koy ve Wand ile çalıştır. Portala attığın eşyaları elfler takas eder: demir → &eElementium&r, elmas → &eDragonstone&r. Kurulum Lexicon'daki 'Alfheim' bölümünde adım adım anlatılıyor.",
    ]),
    Q("bt_gaia", ["kill:botania:doppleganger", "botania:gaia_pylon*8"], title="Gaia Guardian", deps=["bt_alfheim"], shape="gear", size=2.0, rew=["xp:800"], desc=[
        "Botania'nın son boss'u: &eGaia Guardian&r. Bir beacon ve etrafına 8 &eGaia Pylon&r kurar, bir Terrasteel Ingot ile çağırırsın. Seni ışınlar, kopyalar çağırır ve çok sert vurur; arkadaşlarınla birlikte gidin ve iyi zırh giyin. Yendiğinde &eGaia Spirit&r düşürür; bu Botania'nın en güçlü eşyalarının malzemesi.",
    ]),
])

irons = Chapter("irons_spellbooks", "Iron's Spells 'n Spellbooks", "irons_spellbooks:iron_spell_book", "magic", sub="Parşömenler, büyü kitapları ve büyücü zırhları", quests=[
    Q("is_essence", "irons_spellbooks:arcane_essence*8", shape="hexagon", size=1.5, desc=[
        "&eIron's Spells 'n Spellbooks&r'ta büyüler &eparşömenlerde&r (scroll) bulunur: ateş topu, ışınlanma, iyileştirme, yıldırım ve onlarcası. Parşömenleri zindanlardan, büyücü düşmanlardan ve köylülerden elde edersin. Modun ana malzemesi &eArcane Essence&r; büyü kullanan düşmanlardan düşer ve sandıklarda bulunur. JEI'de üzerine gelip &eR&r'ye basarak başka nereden çıktığına bakabilirsin.",
    ]),
    Q("is_book", ["irons_spellbooks:copper_spell_book", "irons_spellbooks:inscription_table"], title="İlk Büyü Kitabı", deps=["is_essence"], rew=["xp:150"], desc=[
        "&eCopper Spell Book&r'u bakır, kağıt ve iple yap. Büyü kitabını Curios yuvasına (envanterdeki ekstra yuvalar) ya da eline al. Sonra &eInscription Table&r'da kitabı ve bir parşömeni birleştirerek büyüyü kitaba kalıcı olarak yaz. Büyü kullanmak için büyü çarkını açıp (tuşunu Ayarlar > Kontroller > Tuşlar'da 'Iron's Spellbooks' altında görebilirsin) büyüyü seçer ve tuşa basarsın. Büyüler mana harcar; ekranın altındaki mavi çubuk manan.",
    ]),
    Q("is_iron_book", ["irons_spellbooks:iron_spell_book", "irons_spellbooks:gold_spell_book"], title="Daha Büyük Kitaplar", deps=["is_book"], desc=[
        "Büyü kitaplarının seviyeleri var: Copper → Iron → Gold → Diamond ve ötesi. Yüksek seviye kitaplar daha fazla büyü yuvası taşır ve bazıları ekstra mana ya da büyü gücü verir. Boss'lardan düşen özel kitaplar (örneğin ölümsüz kralın kitabı) en güçlüleri.",
    ]),
    Q("is_armor", "check", title="Büyücü Zırhları", deps=["is_iron_book"], desc=[
        "Büyücüler için özel zırh setleri var: ateş büyüleri için &ePyromancer&r, buz için &eCryomancer&r, yıldırım için &eElectromancer&r, kutsal büyüler için &ePriest&r ve diğerleri. Her set kendi okulunun büyülerini güçlendirir ve maksimum manayı artırır. Zırhlar büyülü kumaş (Magic Cloth) ve okulun özüyle yapılır, JEI'de 'armor' diye arayarak hepsini görebilirsin. Hangi büyü okulunu sevdiysen ona göre seç.",
    ]),
    Q("is_cauldron", "irons_spellbooks:alchemist_cauldron", deps=["is_book"], desc=[
        "&eAlchemist Cauldron&r ateş üstüne konan büyülü bir kazan. İçine su koyup istenmeyen parşömenleri atarsan onları &emürekkebe&r (ink) çevirir. Mürekkeplerle &eScroll Forge&r'da kendi parşömenlerini yazabilirsin. Kazan ayrıca özel iksirlerin yapımında da kullanılır.",
    ]),
    Q("is_anvil", "irons_spellbooks:arcane_anvil", deps=["is_cauldron"], rew=["xp:200"], desc=[
        "&eArcane Anvil&r ile iki şey yapabilirsin: aynı büyünün iki parşömenini birleştirip &ebir seviye yukarı&r çıkarmak, ve silahlara ya da zırhlara &eUpgrade Orb&r takarak onlara büyü gücü kazandırmak. Böylece normal bir kılıca bile büyü yuvası ekleyebilirsin.",
    ]),
    Q("is_orb", ["irons_spellbooks:upgrade_orb", "irons_spellbooks:arcane_ingot"], title="Upgrade Orb", deps=["is_anvil"], shape="gear", size=1.5, rew=["xp:300"], desc=[
        "&eUpgrade Orb&r, Arcane Ingot, Cinder Essence ve Mithril ile yapılır. Boş orb'u bir okulun rünüyle (örneğin ateş) birleştirip o okulu güçlendiren orb'lar yaparsın; &eMana Upgrade Orb&r ise maksimum manayı artırır. Bunları Arcane Anvil'de zırhlarına tak. Mithril derinlerde, deepslate katmanında bulunan nadir bir cevher.",
    ]),
])

occult = Chapter("occultism", "Occultism", "occultism:dictionary_of_spirits", "magic", sub="Ruhlar, ritüeller ve boyutsal depo", quests=[
    Q("oc_dict", ["occultism:datura_seeds*4", "occultism:dictionary_of_spirits"], title="Dictionary of Spirits", shape="hexagon", size=1.5, desc=[
        "&eOccultism&r ile ruhları çağırıp onlara iş yaptırırsın: maden kazan, eşya taşıyan, takas yapan ruhlar. Önce çimenleri kırarak &eDemon's Dream Seeds&r bul ve bir kitapla birleştirip &eDictionary of Spirits&r kılavuzunu yap. Kitabın 'Getting Started' bölümü her şeyi sırayla anlatıyor, takıldığında oraya bak.",
    ]),
    Q("oc_dream", "occultism:datura*4", title="Demon's Dream", deps=["oc_dict"], desc=[
        "Tohumları ek ve büyüt: &eDemon's Dream&r meyvesi çıkar. Bu meyveyi yediğinde &eThird Eye&r (üçüncü göz) etkisi alırsın ve normalde görünmeyen 'Otherworld' bloklarını görebilir, kazabilirsin. Bazı ağaçların aslında Otherworld ağacı olduğunu ve bazı taşların &eOtherstone&r olduğunu fark edeceksin.",
    ]),
    Q("oc_fire", ["occultism:otherstone*16", "occultism:spirit_attuned_gem"], title="Spiritfire", deps=["oc_dream"], rew=["xp:150"], desc=[
        "Bir Demon's Dream meyvesini yere at ve çakmakla yak: &eSpiritfire&r (ruh ateşi) çıkar. Bu ateş canlılara zarar vermez ama içine attığın eşyaları dönüştürür: taş → &eOtherstone&r, elmas → &eSpirit Attuned Gem&r, ayrıca Otherworld fidanları ve saf tebeşir. Üçüncü göz ile uğraşmadan malzeme toplamanın en kolay yolu.",
    ]),
    Q("oc_chalk", "occultism:chalk_white", title="Tebeşir: White Chalk", deps=["oc_fire"], desc=[
        "Ritüeller için yere &epentacle&r (sihirli desen) çizmen gerekir; bunun için tebeşir lazım. Kalsit tozu ve Otherworld odun tozu ile &eImpure White Chalk&r yap, sonra Spiritfire'a atarak saflaştır: &eWhite Chalk&r. Tebeşirle yere sağ tıklayarak çizersin. İleri ritüeller için altın, mor ve kırmızı tebeşir de gerekecek.",
    ]),
    Q("oc_bowls", ["occultism:sacrificial_bowl*4", "occultism:golden_sacrificial_bowl"], title="Ritüel Kaseleri", deps=["oc_fire"], desc=[
        "Ritüelin merkezine bir &eGolden Ritual Bowl&r, çevresine (8 blok içinde, yeri önemli değil) en az 4 &eSacrificial Bowl&r koy. Malzemeler küçük kaselere, son eşya ise altın kaseye konur. Ritüel sırasında malzemeler tek tek yanar ve ritüel tamamlanır.",
    ]),
    Q("oc_first", ["occultism:book_of_binding_foliot", "check"], title="İlk Ritüel", deps=["oc_chalk", "oc_bowls"], rew=["xp:300"], desc=[
        "Spiritfire'a tüy atarak &eAwakened Feather&r, siyah boya atarak &ePurified Ink&r, kitap atarak &eTaboo Book&r yap ve bunlarla &eBook of Binding: Foliot&r'u hazırla. Kitaptaki 'First Ritual' sayfasını takip ederek ilk ritüelini yap: ilk &eFoliot&r ruhunu çağır! Foliot'lar basit işler yapar: eşya taşımak, cevher kırmak gibi. Ritüeli tamamlayınca bu görevi işaretle.",
    ]),
    Q("oc_soulgem", "occultism:soul_gem", deps=["oc_first"], desc=[
        "&eSoul Gem&r içine bir yaratığı hapsedip başka yere taşımanı sağlar; köylüleri ya da evcil hayvanları taşımak için harika. Bir Djinni ruhu ile yapılan ritüelle hazırlanır, yani önce daha güçlü ruhları çağırmayı öğrenmen gerekiyor.",
    ]),
    Q("oc_storage", ["occultism:storage_controller", "occultism:dimensional_matrix"], title="Boyutsal Depo", deps=["oc_first"], shape="gear", size=1.5, rew=["xp:400"], desc=[
        "Occultism'in en çok sevilen özelliği: &eDimensional Storage Actuator&r. Ruhların koruduğu bir cep boyutunda binlerce eşya saklar ve hepsini tek bir ekranda aranabilir şekilde gösterir; Refined Storage'a büyülü bir alternatif. &eDimensional Crystal Matrix&r ile yapılır ve stabilizatörlerle kapasitesi artırılır. Eşyaları otomatik getiren ruhlar bile ekleyebilirsin.",
    ]),
])

MAGIC = [ars, botania, irons, occult]
