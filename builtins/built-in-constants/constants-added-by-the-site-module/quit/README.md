## `quit()`

```
quit(code=None)
exit(code=None)
```

Objects that when printed, print a message like "Use quit() or Ctrl-D
(i.e. EOF) to exit", and when accessed directly in the interactive
interpreter or called as functions, raise [SystemExit](https://docs.python.org/3.15/builtins/exceptions.html#SystemExit) with the
specified exit code.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:1.7.1: quit etkileşimini ayır**

#### Önce

[b:1.7](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

quit nesnesini yazdırma ile quit(3) çağrısını, ardından exit(3) eşdeğerini karşılaştır. Çıkış kodunu ve kontrol akışını yazılı göster.

#### Geçiş ölçütleri

- [ ] Yazdırma kullanım mesajını gösterir; çağrı code=3 olan SystemExit yükseltir; exit aynı işlevidir.
- [ ] Etkileşimli yardımcı ile uygulamanın iş mantığı birbirine karıştırılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../help/README.md)
<!-- learning-task:end -->
