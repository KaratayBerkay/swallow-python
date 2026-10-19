## 12.1. Introduction

Python applications will often use packages and modules that don't come as part of the standard library. Applications will sometimes need a specific version of a library, because the application may require that a particular bug has been fixed or the application may be written using an obsolete version of the library's interface.

This means it may not be possible for one Python installation to meet the requirements of every application. If application A needs version 1.0 of a particular module but application B needs version 2.0, then the requirements are in conflict and installing either version 1.0 or 2.0 will leave one application unable to run.

The solution for this problem is to create a virtual environment, a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages.

Different applications can then use different virtual environments. To resolve the earlier example of conflicting requirements, application A can have its own virtual environment with version 1.0 installed while application B has another virtual environment with version 2.0. If application B requires a library be upgraded to version 3.0, this will not affect application A's environment.

<!-- learning-task:start -->
### Bölüm görevi

**Görev 12.1: Çakışan bağımlılığı iki ortamda ayır**

**Odak:** Sürüm çatışması ve sanal ortamın uygulama başına izolasyonu.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:10.12](../../10-brief-tour-of-the-standard-library/10.12-batteries-included/README.md).

#### Tek görev

1. Kod veya kurulum yapmadan şu durumun ortam çizimini hazırla: A uygulaması lib 1.0, B uygulaması lib 2.0 istiyor; sonra B 3.0 istiyor.

2. Önce tek ortamda çatışmayı, sonra iki ayrı ortamda paket yerleşimini göster.

3. Python yorumlayıcı sürümü ile paketin sürümünü çizimde ayrı etiketle.

#### Geçiş ölçütleri

- [ ] A ve B için ayrı bağımlılık alanları var; B yükselmesi A ortamını değiştirmiyor.
- [ ] Tek ortamın aynı ihtiyaçları neden karşılayamayacağı belirtilmiş.
- [ ] Sanal ortam paket sürümü ile Python sürümü karıştırılmamış; henüz öğretilmeyen komutlar gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../12.2-creating-virtual-environments/README.md)
<!-- learning-task:end -->
