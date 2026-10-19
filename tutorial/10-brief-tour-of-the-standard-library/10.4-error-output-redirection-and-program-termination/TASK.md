# Görev 10.4: Hata mesajıyla normal çıktıyı ayır

**Odak:** stdout/stderr ayrımı ve sys.exit ile yürütmeyi bitirme.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:10.3](../10.3-command-line-arguments/README.md).
- Ön bilgi: [t:8.4](../../08-errors-and-exceptions/8.4-raising-exceptions/README.md).

## Tek görev

1. Küçük betikte print ile "starting" yaz; sys.stderr.write ile "missing data\n" yaz; sys.exit() çağır; arkasına print("unreachable") koy.

2. Terminalde dene ve her mesajın akışını not et.

3. Normal çıktı bir dosyaya yönlendirilmiş olsaydı hangi mesajın dosyaya, hangisinin stderr akışına gideceğini açıkla. Shell yönlendirme komutu yazman gerekmiyor.

## Geçiş ölçütleri

- [ ] starting stdout, missing data stderr üzerinden; unreachable basılmıyor.
- [ ] sys.exit sonrasına normal yürütmeyle geçilmiyor.
- [ ] Hata mesajının sıradan printten ayrı akışa yazılmasının amacı açıklanmış.
- [ ] stdout yönlendirilse stderr görünürlüğünün ayrı kaldığı kavramsal olarak gösterilmiş; yeni shell yönlendirme sözdizimi gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
