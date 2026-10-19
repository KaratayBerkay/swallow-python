## 10.7. Internet access

There are a number of modules for accessing the internet and processing internet protocols. Two of the simplest are `urllib.request` for retrieving data from URLs and `smtplib` for sending mail:

``` python
>>> from urllib.request import urlopen
>>> with urlopen('https://docs.python.org/3/') as response:
...     for line in response:
...         line = line.decode()             # Convert bytes to a str
...         if 'updated' in line:
...             print(line.rstrip())         # Remove trailing newline
...
      Last updated on Nov 11, 2025 (20:11 UTC).

>>> import smtplib
>>> server = smtplib.SMTP('localhost')
>>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
... """To: jcaesar@example.org
... From: soothsayer@example.org
...
... Beware the Ides of March.
... """)
>>> server.quit()
```
> Code: [server.py](server.py)

(Note that the second example needs a mailserver running on localhost.)

<!-- learning-task:start -->
### Bölüm görevi

**Görev 10.7: Ağ örneğinin veri ve yan etki izini çıkar**

**Odak:** urlopen yanıtı, bytes decode, satır filtresi, bağlam kapatma ve SMTP gönderim akışı.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:7.2.1](../../07-input-and-output/7.2-reading-and-writing-files/7.2.1-methods-of-file-objects/README.md).
- Ön bilgi: [t:10.6](../10.6-mathematics/README.md).

#### Tek görev

1. Ağ bağlantısı açmadan README örneğinin izini çıkar.

2. Yanıt satırlarını [b"Title\n", b"Last updated today\n"] kabul et; bölümdeki decode, "updated" filtresi ve rstrip işlemlerini bu liste üzerinde uygula.

3. SMTP örneğini yalnız kâğıt üzerinde SMTP bağlantısı, sendmail alıcı/gönderici/mesajı ve quit adımlarına ayır.

4. Taslakta gönderim yapan kodu çalıştırma; uzak işlem yapılmadan veri ve etki ayrımı değerlendiriliyor.

#### Geçiş ölçütleri

- [ ] Yerel çıktı yalnız Last updated today; decode öncesi bytes, sonrası str.
- [ ] Satır sonunu kaldırma ile filtreleme ayrı işlemler olarak açıklanmış.
- [ ] with yanıt kaynağını kapatıyor; SMTP quit bağlantıyı bitiriyor.
- [ ] SMTP örneğinin sunucu gereksinimi ve sendmail çağrısının dış dünyaya mesaj gönderdiği doğru işaretlenmiş.
- [ ] Gerçek ağ servisi, e-posta hesabı veya gönderim gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../10.8-dates-and-times/README.md)
<!-- learning-task:end -->
