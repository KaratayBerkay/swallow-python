## 11.4. Multi-threading

Threading is a technique for decoupling tasks which are not sequentially dependent. Threads can be used to improve the responsiveness of applications that accept user input while other tasks run in the background. A related use case is running I/O in parallel with computations in another thread.

The following code shows how the high level `threading` module can run tasks in background while the main program continues to run:

``` python
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        super().__init__()
        self.infile = infile
        self.outfile = outfile

    def run(self):
        with zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED) as f:
            f.write(self.infile)
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')
```
> Code: [init.py](init.py)

The principal challenge of multi-threaded applications is coordinating threads that share data or other resources. To that end, the threading module provides a number of synchronization primitives including locks, events, condition variables, and semaphores.

While those tools are powerful, minor design errors can result in problems that are difficult to reproduce. So, the preferred approach to task coordination is to concentrate all access to a resource in a single thread and then use the `queue` module to feed that thread with requests from other threads. Applications using `Queue` objects for inter-thread communication and coordination are easier to design, more readable, and more reliable.

<!-- learning-task:start -->
### Bölüm görevi

**Görev 11.4: Eşzamanlı akışta yalnız garanti edilen sırayı yaz**

**Odak:** Thread.start, arka plan run, join ve paylaşılan kaynak koordinasyonu.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:11.3](../11.3-working-with-binary-data-record-layouts/README.md).
- Ön bilgi: [t:9.5](../../09-classes/9.5-inheritance/README.md).

#### Tek görev

1. README içindeki AsyncZip sınıfını hazır örnek olarak incele.

2. Asıl örnekte üç mesaj için mümkün sıraları yaz: "Finished background zip", "The main program continues", "Main program waited".

3. Ayrı bir senkron sürümde aynı AsyncZip nesnesinin oluşturulmasından sonraki kodu aşağıdaki üç satırla değiştir. Bu sürümde start ve join çağrısı yok. Mesaj sırasını asıl örnekle karşılaştır:

```python
background.run()
print('The main program continues to run in foreground.')
print('Synchronous call finished.')
```

4. Paylaşılan tek dosyaya birden fazla thread yazması halinde bölümde önerilen tek kaynak sahibi thread + queue düzenini çiz. Thread veya zipfile iç APIlerini genişletmen gerekmiyor.

#### Geçiş ölçütleri

- [ ] Asıl örnekte ilk iki mesajın sırası garanti edilmemiş; son mesaj her ikisinden sonra.
- [ ] Asıl örnekte start yeni akışı başlatıyor; join arka plan bitene kadar bekliyor.
- [ ] Senkron sürümde Finished background zip, The main program continues, Synchronous call finished sırası kesin; run normal metot çağrısı olarak bitmeden sonraki satıra geçilmiyor.
- [ ] Kuyruk ile tek kaynak sahibi yaklaşımının çakışan erişimi nasıl azalttığı açıklanmış; lock algoritması istenmemiş.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../11.5-logging/README.md)
<!-- learning-task:end -->
