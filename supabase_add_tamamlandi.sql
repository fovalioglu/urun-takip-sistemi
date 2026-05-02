-- Supabase: urunler tablosuna tamamlanma bayrağı (boolean, varsayılan false).
-- SQL düzenleyicide bir kez çalıştırın.

alter table public.urunler
  add column if not exists tamamlandi boolean not null default false;

comment on column public.urunler.tamamlandi is
  'Ürün satırı tamamlandı olarak işaretlendi mi (varsayılan: hayır).';
