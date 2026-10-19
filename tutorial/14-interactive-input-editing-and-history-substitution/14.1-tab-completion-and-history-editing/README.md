## 14.1. Tab Completion and History Editing

Completion of variable and module names is automatically enabled at interpreter startup so that the Tab key invokes the completion function; it looks at Python statement names, the current local variables, and the available module names. For dotted expressions such as `string.a`, it will evaluate the expression up to the final `'.'` and then suggest completions from the attributes of the resulting object. Note that this may execute application-defined code if an object with a `__getattr__()` method is part of the expression. The default configuration also saves your history into a file named `.python_history` in your user directory. The history will be available again during the next interactive interpreter session.

<!-- learning-task:start -->
### Bölüm görevi

**Görev 14.1: Tamamlama kaynağını ve geçmişi tanı**

**Odak:** Yerel/modül adlarını tamamlama, noktalı nitelikler ve oturumlar arası geçmiş.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:14](../README.md).
- Ön bilgi: [t:6.3](../../06-modules/6.3-the-dir-function/README.md).

#### Tek görev

1. REPL içinde lesson_marker = 7 tanımla; lesson_m önekinden Tab tamamlamasını dene.

2. Bilinen bir modülün noktalı ifadesi için önerilerin nereden geldiğini açıkla.

3. Yeni oturumda geçmiş davranışını gözlemle; destek yoksa bunu ortam sınırı olarak kaydet.

4. README içindeki noktalı ifade değerlendirmesinin neden yalnız metin araması olmadığını anlat.

#### Geçiş ölçütleri

- [ ] Yerel ad tamamlama kaynağı olarak doğru; modül/nitelik kaynağı ayrı.
- [ ] Geçmişin .python_history ile ilişkilendirildiği, tüm kurulumlarda aynı gözlemin dayatılmadığı belirtilmiş.
- [ ] Noktanın solundaki nesnenin değerlendirilmesinin kullanıcı kodunu çalıştırabileceği kaynak notuyla ilişkilendirilmiş.
- [ ] `__getattr__` uygulaması yazmak veya kullanıcı profilini değiştirmek gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../14.2-alternatives-to-the-interactive-interpreter/README.md)
<!-- learning-task:end -->
