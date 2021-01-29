![alt text](https://www.haberso.com/sites/367/uploads/2020/11/10/large/baabfca6e9e1d4e3-1605011750.jpg?)

# Kardiyovasküler Hastalık Teşhisi Modeli

Günümüz bilgisayarları insana nazaran daha hızlı işlem yapabilmektedir ancak karar verme yetenekleri insana göre daha düşüktür.
Bu nedenle bilgisayarların daha iyi analizler yapıp kararlar verebilmelerini sağlayan farklı makine öğrenmesi teknikleri geliştirilmiş ve
geliştirilmektedir. Kümeleme, sınıflama yöntemleri, karar ağaçları, yapay sinir ağları gibi pek çok teknik ile veriden anlam çıkarımı ve
tahminleme yapılabilmektedir. Makine öğrenmesi tekniklerinin, başarılı sınıflama ve tanılama yetenekleri ile hastalık teşhisinde
medikal uzmanlara yardımcı olarak kullanımları da hızla artmaktadır.

Dünya genelindeki ölümler en sık kardiyovasküler hastalıklar (KVH) sebebiyledir. Dünya Sağlık
Örgütü (DSÖ) verilerine göre 2012 yılında tahminen 17,5 milyon insan KVH’ler nedeniyle yaşamını
yitirmiştir ki, bu tüm ölümlerin %31’ine tekabül etmektedir. Bu ölümlerin de %80’i kalp krizi ve inmeye bağlı olarak gelişmiştir. Ülkemizde ise Türkiye İstatistik Kurumu (TÜİK) verilerine göre 2016 yılında ölüm nedenleri içerisinde dolaşım sistemi hastalıkları nedeniyle gerçekleşen ölüm vakaları tüm ölümlerin %39,8’ini oluşturarak ilk sırada yer
almıştır.
KVH açısından olumlu olan bir husus ise büyük ölçüde önlenebilir olmalarıdır. DSÖ, kan basıncı (KB),
obezite, kolesterol ve sigara kullanımının kontrolü ile KVH’lerin görülme sıklığının yarıya indirilebileceğini bildirmektedir. Bu sebeple KVH açısından yüksek riskli bireylerin erken tespit edilip korunmalarının sağlanması akılcı olacaktır.
KVH’lerden korunmada yaklaşım tarzı çoğul risk
faktörleri gözetilerek genel riskin düşürülmesine
yönelik ve multidisipliner olmalıdır. KVH’lerin
bireysel olarak azaltılmasını sağlamak için öncelikle riskleri belirlemek gerekmektedir. Bu amaçla
sosyodemografik ve tıbbi bilgileri içeren bir hastahekim görüşmesini, fizik muayene ve laboratuvar
verileriyle destekleyerek değerlendirmek gerekmektedir.

Artık günümüz teknolojisinde tıp dünyasında profosyonel olarak özellikle ekg, floroskopi, kanser teşhisi vb. alanlarda benzer çalışmalar sıklıkla gerçekleştirilmektedir (bkz:https://www.nature.com/articles/s41467-020-15432-4). Bu tür modeller bazen hastaya zaman ve paradan tasarruf ettiriyor olsa bile bazen ise verimli olmayabilir. Modelin, tipik tıbbi muayeneden daha hızlı ve kolay bir şekilde elde edilebilen verilerle benzer bir doğruluk düzeyine ulaşabileceğini gösterebilirsek, o zaman bu teknoloji teşhis sürecini kolaylaştırabilir.

Bu projede ise hem geleneksel makine öğrenmesi modellerini(Lojistik Regresyon, Destek Vektör Makineleri vb.) kullanarak hemde güncel modelleri(LightGBM,XGBoost,AdaBoost) kullanarak KVH tespiti yapmaya çalıştım. Tamamen bilimsel ve istatistiksel olarak probleme yaklaşmaya çalıştım fakat insan sağlığı söz konusu olduğu için asla sonuçlara güvenilmesini şahsen önermemekteyim eğer böyle bir rahatsızlığınızın olduğunu düşünüyorsanız bu durumu sosyodemografik ve tıbbi bilgileri içeren bir hastahekim görüşmesi ile ve fizik muayene ve laboratuvar verileriyle destekleyerek değerlendirmek gerekmektedir.

# Veriseti
Verisetimiz yaklaşık olarak 70.000 gerçek hasta verilerinden oluşturulmuştur veriyi Kaggle adlı siteden Svetlana Ulianova isimli kullanıcının kaynağından aldım. Burada yapmak istediğim sadece bir sınıflandırma modeli oluşturmak değil aynı zamanda hangi verilerin ve hangi tür özellikler(muayane, demografik, sosyal yaşam) KVH oluşumunda kaydadeğer yararının olduğunu öğrenmekti. Verisetimiz 11 özelliğe sahip ve 34,979 KVH sahip ve 35,021 KVH sahip olmayan hasta var biz ise bu verilerle modelimizi eğitip başarımı yüksek bir sonuç almayı hedefliyoruz.

Verinin Tanımlanması:
- Yaş(Demografik)
- Boy(Demografik)
- Kilo(Demografik)
- Cinsiyet(Demografik)
- Sistolik kan basıncı(Muayene)
- Diyastolik kan basıncı(Muayene)
- Kolesterol(Muayene)
- Glikoz(Muayene)
- Sigara(Sosyal Yaşam)
- Alkol(Sosyal Yaşam)
- Fiziksel Aktivite(Sosyal Yaşam)
- KVH durumu

(Tüm veri seti değerleri tıbbi muayene anında toplanmıştır.)


