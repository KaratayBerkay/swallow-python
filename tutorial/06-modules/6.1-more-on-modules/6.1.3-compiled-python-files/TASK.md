# Görev 6.1.3: Önbelleğin neyi hızlandırdığını ayır

**Odak:** .pyc, sürüm etiketi, kaynak değişimi, doğrudan betik, -O/-OO ve derleme/yürütme ayrımı.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:6.1.2](../6.1.2-the-module-search-path/README.md).

## Tek görev

1. counts.py için dört durumlu karar tablosu hazırla: önbellek yokken ilk import; aynı kaynak ve geçerli önbellekle yeni yorumlayıcıda import; kaynağın değişiklik tarihi değişip önbellek eski kaldığında yeni yorumlayıcıda import; dosyayı doğrudan betik olarak çalıştırma. Normal, önbellek yazılabilen bir çalışma klasörü varsay.

2. Her satırda kaynak derlenir mi, `__pycache__` kullanılabilir mi ve işlevin çalışma hızı hakkında ne söylenebilir yaz.

3. Kaynaksız dağıtımın özel yerleşimini, sürüm etiketini ve -O/-OO farkını ayrıca açıklayıp compileall aracının amacını belirt.

4. Kurulu dosyalarda önbellek silmen gerekmiyor.

## Geçiş ölçütleri

- [ ] Verilen eski önbellek durumunda kaynak yeniden derleniyor; geçerli önbellek durumunda derlenmiş sürüm kullanılabiliyor. Karar, anlatımdaki değişiklik tarihi denetimine dayandırılmış.
- [ ] Aynı oturumdaki import cache ile disk bytecode cache ayrılmış.
- [ ] Doğrudan çalıştırılan ana betik için normal modül cache davranışı varsayılmamış.
- [ ] .pyc yüklemeyi hızlandırır; aynı kodun yürütmesini kendiliğinden hızlandırmaz.
- [ ] Sürüm etiketleri, kaynak olmadan .pyc yerleşimi ve platform bağımsızlığı doğru.
- [ ] -O assert, -OO ayrıca docstring kaldırma; compileall toplu derleme olarak açıklanmış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
