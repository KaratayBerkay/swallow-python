# Milestone: Tür açıklamasının ağacını çöz

## Önce

Bu klasördeki bütün bölüm görevleri ve alt klasör milestone kontrolleri tamamlanmış olmalı. Sırayı [görev dizininden](../../../TASKS.md) kontrol et.

## Tek görev

dict[str,list[int]] açıklamasını origin/args üzerinden iki seviyede çöz; list[T] içindeki serbest parametreyi somut intle değiştirince __parameters__ sonucunu göster. Normal ve unpacked alias işaretini karşılaştır; int|str için geçerli runtime denetimini generic list denetimiyle ayır.

## Geçiş ölçütleri

- [ ] Tür açıklaması veri dönüşümü veya otomatik öğe denetimi sayılmamıştır.
- [ ] Origin/args/parameters/unpacked farklı bilgileri taşır; parameterized generic ile isinstance TypeError sınırı korunur.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
