# Görev 16.1.3: Başlangıç dosyasının hangi oturumda çalışacağını çıkar

**Odak:** PYTHONSTARTUP, aynı namespace, etkileşimli/betik farkı ve açık yükleme.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:16.1.2](../16.1.2-executable-python-scripts/README.md).
- Ön bilgi: [t:6.2](../../../06-modules/6.2-standard-modules/README.md).

## Tek görev

1. Yerel bir startup taslağına marker = "ready" yaz.

2. Değişiklik yapmadan üç çalıştırmanın izini çıkar: PYTHONSTARTUP bu dosyayı gösterirken etkileşimli başlangıç; normal betik çalıştırma; README içindeki açık dosya okuma/exec iskeletini içeren betik. marker hangi durumda kullanılabilir?

3. Dosya yolu tanımlı değilken veya dosya yokken iskeletin ne yaptığını da açıkla.

## Geçiş ölçütleri

- [ ] Normal etkileşimli başlangıç marker bağını aynı namespace içine ekliyor.
- [ ] Normal betik başlangıç dosyasını kendiliğinden çalıştırmıyor; açık yükleyen betik çalıştırıyor.
- [ ] Dosya tanımsız/yoksa koşullu gövdeye girilmiyor.
- [ ] İstemlerin de bu dosyada değiştirilebildiği ve /dev/tty istisnası belirtilmiş; shell profiline kalıcı ayar yazılmamış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
