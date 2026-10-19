## 11.5. Logging

The `logging` module offers a full featured and flexible logging system. At its simplest, log messages are sent to a file or to `sys.stderr`:

``` python
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')
```
> Code: [logging_example.py](logging_example.py)

This produces the following output:

``` text
WARNING:root:Warning:config file server.conf not found
ERROR:root:Error occurred
CRITICAL:root:Critical error -- shutting down
```

By default, informational and debugging messages are suppressed and the output is sent to standard error. Other output options include routing messages through email, datagrams, sockets, or to an HTTP Server. New filters can select different routing based on message priority: `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL`.

The logging system can be configured directly from Python or can be loaded from a user editable configuration file for customized logging without altering the application.

<!-- learning-task:start -->
### Bölüm görevi

**Görev 11.5: Görünmeyen kayıtla çalışmayan kodu karıştırma**

**Odak:** Logging öncelikleri, varsayılan eşik, stderr ve mesaj yerleştirme.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:11.4](../11.4-multi-threading/README.md).
- Ön bilgi: [t:10.4](../../10-brief-tour-of-the-standard-library/10.4-error-output-redirection-and-program-termination/README.md).

#### Tek görev

1. Yeni bir betikte debug, info, warning, error ve critical seviyelerinde kendine ait beş mesaj üret. warning mesajına bölümdeki %s yöntemiyle "lesson.conf" değerini geçir.

2. Varsayılan yapılandırmada hangi mesajların çıktığını önce yaz, sonra çalıştır.

3. Bastırılan mesajların kodunun çalışmadığı sonucunun neden çıkarılamayacağını açıkla.

#### Geçiş ölçütleri

- [ ] WARNING, ERROR, CRITICAL mesajları var; DEBUG ve INFO görünmüyor.
- [ ] Yerleştirilen dosya adı lesson.conf; log mesajı ile seviye ayrı.
- [ ] Varsayılan hedef stderr; ayrı yapılandırılmış oturum davranışı bu deneyle karıştırılmamış.
- [ ] Öncelik filtresi ile program yürütme koşulu ayrılmış; henüz gösterilmeyen handler yapılandırması istenmemiş.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../11.6-weak-references/README.md)
<!-- learning-task:end -->
