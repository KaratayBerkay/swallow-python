## 10.12. Batteries included

Python has a "batteries included" philosophy. This is best seen through the sophisticated and robust capabilities of its larger packages. For example:

- The `xmlrpc.client` and `xmlrpc.server` modules make implementing remote procedure calls into an almost trivial task. Despite the modules' names, no direct knowledge or handling of XML is needed.

- The `email` package is a library for managing email messages, including MIME and other [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html)-based message documents. Unlike `smtplib` and `poplib` which actually send and receive messages, the email package has a complete toolset for building or decoding complex message structures (including attachments) and for implementing internet encoding and header protocols.

- The `json` package provides robust support for parsing this popular data interchange format. The `csv` module supports direct reading and writing of files in Comma-Separated Value format, commonly supported by databases and spreadsheets. XML processing is supported by the `xml.etree.ElementTree`, `xml.dom` and `xml.sax` packages. Together, these modules and packages greatly simplify data interchange between Python applications and other tools.

- The `sqlite3` module is a wrapper for the SQLite database library, providing a persistent database that can be updated and accessed using slightly nonstandard SQL syntax.

- Internationalization is supported by a number of modules including `gettext`, `locale`, and the `codecs` package.

<!-- learning-task:start -->
### Bölüm görevi

**Görev 10.12: İhtiyaca uygun standart modülü seç**

**Odak:** Standart kitaplık yeteneklerini tanıma; mesaj yapısı, aktarım, veri biçimi ve saklama ayrımı.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:10.11](../10.11-quality-control/README.md).

#### Tek görev

1. Kod yazmadan şu ihtiyaçları bölümde adı geçen araçlarla eşleştir: e-posta eklerini çözmek; e-postayı göndermek; CSV tablosunu okumak; JSON verisini aktarmak; XML ağacını işlemek; yerel kalıcı ilişkisel veri; çevrilebilir mesajlar; uzaktaki işlevi çağırmak.

2. Her seçimde neyin sorumluluk dışında kaldığını bir cümleyle belirt.

#### Geçiş ölçütleri

- [ ] email mesaj yapısı, smtplib gönderim olarak ayrılmış.
- [ ] csv, json, XML paketleri, sqlite3, gettext ve xmlrpc görevleriyle eşleşmiş.
- [ ] Modül adı tanıma ile API kullanabilmenin aynı olmadığı belirtilmiş.
- [ ] Bu bölüm yalnız yetenek tanıttığı için SQL, XML veya ağ protokolü kodu istenmemiş.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
