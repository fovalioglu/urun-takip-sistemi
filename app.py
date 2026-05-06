from __future__ import annotations

from dotenv import load_dotenv
import os

load_dotenv()

# environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# eğer değer yoksa hata ver
if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Supabase environment variables eksik")

import streamlit as st

st.set_page_config(
    page_title="Laperissa",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>
:root{
--ui-text-strong:#111827;
--ui-text-muted:#374151;
}

/* ANA ARKA PLAN */
[data-testid="stAppViewContainer"]{
background: linear-gradient(
135deg,
#f4f6fb 0%,
#eef2f9 35%,
#e9eef7 60%,
#f7f9fc 100%
);
color:#1f2937;
}

/* Bilgi metinleri / label'lar: yüksek kontrast, soluk görünüm kapalı */
[data-testid="stCaptionContainer"],
[data-testid="stCaptionContainer"] *,
.stMarkdown p,
.stMarkdown span,
[data-testid="stMarkdownContainer"],
[data-testid="stMarkdownContainer"] *,
[data-testid="stMetricLabel"],
[data-testid="stMetricLabel"] *,
[data-testid="stMetricValue"],
[data-testid="stMetricValue"] *,
[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] *,
[data-testid="stCheckbox"] label,
[data-testid="stCheckbox"] label *,
[data-baseweb="checkbox"] label,
[data-baseweb="checkbox"] label *,
[data-testid="stTextInput"] label,
[data-testid="stTextArea"] label,
[data-testid="stSelectbox"] label,
[data-testid="stNumberInput"] label,
[data-testid="stDateInput"] label,
[data-testid="stMultiSelect"] label,
[data-testid="InputInstructions"],
[data-testid="InputInstructions"] *,
[data-testid="stHelpText"],
[data-testid="stHelpText"] *,
small,
p small,
label{
color:var(--ui-text-strong) !important;
opacity:1 !important;
font-weight:500 !important;
text-shadow:none !important;
}

/* Secondary text tonu (hala okunaklı) */
[data-testid="stCaptionContainer"] em,
[data-testid="stHelpText"] em,
[data-testid="InputInstructions"] em{
color:var(--ui-text-muted) !important;
opacity:1 !important;
}

/* Küçük bilgi yazıları responsive'de kaybolmasın */
[data-testid="stCaptionContainer"],
[data-testid="stCaptionContainer"] p,
[data-testid="stCaptionContainer"] span,
.stMarkdown p,
.stMarkdown span,
[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] span,
small{
white-space:normal !important;
overflow-wrap:anywhere !important;
word-break:break-word !important;
}

/* Disabled solukluğu kaldır (özellikle checkbox/select etiketleri) */
[data-baseweb="checkbox"] *,
[data-baseweb="select"] *,
[aria-disabled="true"]{
opacity:1 !important;
color:var(--ui-text-strong) !important;
}

/* ANA İÇERİK GENİŞLİĞİ — tablo için maksimum yatay alan */
.block-container{
max-width: 100% !important;
padding-left:12px !important;
padding-right:12px !important;
padding-top:25px;
}

/* LOGIN KART (Streamlit form) */
section.main [data-testid="stForm"]{
background:#ffffff;
padding:40px;
border-radius:18px;
width:420px;
max-width:100%;
margin-left:auto;
margin-right:auto;
box-shadow:0 10px 30px rgba(15,23,42,0.08);
}

/* LOGO */
.login-logo{
display:block;
margin:auto;
width:160px;
margin-bottom:20px;
}

/* INPUT LABEL */
label{
color:#1f2937 !important;
font-weight:500;
}

input::placeholder{
color:#6b7280;
}

/* kartlar */
.stButton>button{
background:#111827;
color:white;
}

/* Global dark/primary button text contrast fix */
.stButton button,
button[kind="primary"],
div[data-testid="stDownloadButton"] button,
div[data-testid="baseButton-primary"]{
color:#ffffff !important;
-webkit-text-fill-color:#ffffff !important;
opacity:1 !important;
font-weight:600 !important;
}

/* Buton içi ikonlar da beyaz */
.stButton button svg,
button[kind="primary"] svg,
div[data-testid="stDownloadButton"] button svg,
div[data-testid="baseButton-primary"] svg{
color:#ffffff !important;
fill:#ffffff !important;
stroke:#ffffff !important;
opacity:1 !important;
}

/* Hover'da text kaybolmasın */
.stButton button:hover,
button[kind="primary"]:hover,
div[data-testid="stDownloadButton"] button:hover,
div[data-testid="baseButton-primary"]:hover{
color:#ffffff !important;
-webkit-text-fill-color:#ffffff !important;
opacity:1 !important;
}

/* filtre alanları */
[data-baseweb="select"]{
background:white;
border-radius:8px;
}

/* Global selectbox contrast fix (dark input uyumlu) */
div[data-baseweb="select"] span,
div[data-baseweb="select"] input,
div[data-baseweb="select"] div,
div[data-baseweb="select"] svg{
color:#ffffff !important;
-webkit-text-fill-color:#ffffff !important;
opacity:1 !important;
}
div[data-baseweb="select"] svg{
fill:#ffffff !important;
}
/* Placeholder açık gri kalsın */
div[data-baseweb="select"] input::placeholder{
color:#d1d5db !important;
-webkit-text-fill-color:#d1d5db !important;
opacity:1 !important;
}
/* Selected value ve dropdown option metinleri beyaz */
div[data-baseweb="select"] [role="combobox"],
div[data-baseweb="select"] [role="combobox"] *{
color:#ffffff !important;
-webkit-text-fill-color:#ffffff !important;
opacity:1 !important;
}
[role="listbox"] [role="option"],
ul[role="listbox"] li,
div[role="option"],
div[role="option"] *{
color:#ffffff !important;
-webkit-text-fill-color:#ffffff !important;
opacity:1 !important;
}

/* tablo / düzenleyici — tam genişlik */
[data-testid="stDataFrame"],
[data-testid="stDataEditor"]{
background:white;
border-radius:12px;
padding:10px;
width:100% !important;
max-width:100% !important;
}

.stDataFrame,
[data-testid="stDataEditor"] > div{
width:100% !important;
max-width:100% !important;
}

/* üst filtre satırı da genişlesin */
[data-testid="column"]{
padding-left:8px;
padding-right:8px;
}

/* scroll alanını optimize et */
section.main > div{
max-width:100% !important;
}

/* gereksiz marginleri temizle */
.css-18e3th9{
padding-left:12px !important;
padding-right:12px !important;
}

/* başlık alt yazı */
.css-10trblm{
color:var(--ui-text-muted);
font-weight:500;
}

/* input alanları */
input{
background:white !important;
color:#111827 !important;
border:1px solid #d1d5db !important;
}

/* genel font rengi */
body{
color:var(--ui-text-strong);
}

/* Streamlit default secondary text tonlarını güçlendir */
p, small, .stText, .stCaption{
color:var(--ui-text-strong) !important;
font-weight:500 !important;
}

/* Metric alanı: etiket koyu, değer tam siyah */
[data-testid="stMetricLabel"]{
color:#374151 !important;
opacity:1 !important;
font-weight:600 !important;
}
[data-testid="stMetricValue"],
[data-testid="stMetricValue"] *{
color:#111827 !important;
opacity:1 !important;
font-weight:700 !important;
}

/* Checkbox label'ları özellikle görünür kalsın */
[data-testid="stCheckbox"] label p,
[data-baseweb="checkbox"] label p{
color:#111827 !important;
opacity:1 !important;
font-weight:600 !important;
}

/* Streamlit muted/secondary metin override */
[class*="secondary"],
[class*="muted"],
[data-testid="stCaptionContainer"]{
color:#374151 !important;
opacity:1 !important;
}

::-webkit-scrollbar{
height:8px;
}

</style>
""",
    unsafe_allow_html=True,
)

import datetime
import html
import time
from io import BytesIO, StringIO
from pathlib import Path
import pandas as pd

from supabase import create_client

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def update_online_status(username: str) -> None:
    try:
        supabase.table("online_users").upsert(
            {
                "username": username,
                "last_seen": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            }
        ).execute()
    except Exception:
        pass


def get_online_users() -> list[str]:
    try:
        threshold = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(
            seconds=90
        )
        response = (
            supabase.table("online_users")
            .select("username,last_seen")
            .gte("last_seen", threshold.isoformat())
            .execute()
        )
        rows = response.data or []
        return [str(u["username"]) for u in rows]
    except Exception:
        return []


def render_online_users() -> None:
    if "user" not in st.session_state:
        return
    update_online_status(str(st.session_state["user"]))
    online_users = get_online_users()
    online_count = len(online_users)
    if hasattr(st, "popover"):
        with st.popover(f"🟢 {online_count} online"):
            if online_users:
                for u in online_users:
                    st.write("🟢", u)
            else:
                st.caption("kimse online değil")
    else:
        with st.expander(f"🟢 {online_count} online", expanded=False):
            if online_users:
                for u in online_users:
                    st.write("🟢", u)
            else:
                st.caption("kimse online değil")


COL_DAB = "D-A=T"
COL_SB_ID = "id"
COL_CREATED = "Oluşturulma"
COL_URUN = "Ürün Kodu"  # Supabase: stok_kodu
COL_URUN_ADI = "Ürün Adı"  # urun_adi
COL_BEDEN = "Beden"
COL_ATOLYE = "Atölye"
COL_PLM = "PLM"
COL_RENK = "Renk"
COL_KESIM = "Kesim Adedi"
COL_FASON = "Fason Durum"
COL_DSM = "DSM Termin"
COL_ATOLYE_TERM = "Atölye Termin"
COL_TAMAMLANDI = "Tamamlandı"
COL_AUDIT = "Son değişiklik"

SB_TABLE_URUNLER = "urunler"
SB_TO_APP: dict[str, str] = {
    "id": COL_SB_ID,
    "created_at": COL_CREATED,
    "urun_adi": COL_URUN_ADI,
    "stok_kodu": COL_URUN,
    "beden": COL_BEDEN,
    "renk": COL_RENK,
    "atolye": COL_ATOLYE,
    "plm": COL_PLM,
    "kesim_adedi": COL_KESIM,
    "fason_durum": COL_FASON,
    "dsm_termin": COL_DSM,
    "atolye_termin": COL_ATOLYE_TERM,
    "tamamlandi": COL_TAMAMLANDI,
}
APP_TO_SB: dict[str, str] = {app: sb for sb, app in SB_TO_APP.items()}
KULLANICI_TABLO = "admin"
USER_FILE = "users.csv"
VERILER_CSV = "veriler.csv"


def _coerce_bool_loose(val: object) -> bool:
    if val is True or val is False:
        return bool(val)
    if val is None or val is pd.NA:
        return False
    if isinstance(val, float) and pd.isna(val):
        return False
    if isinstance(val, (int, float)) and not isinstance(val, bool):
        try:
            return int(val) != 0
        except (TypeError, ValueError):
            return False
    sl = str(val).strip().lower()
    if sl in ("true", "1", "yes", "evet", "x"):
        return True
    return False
# İlk kurulumda boş users.csv için örnek hesaplar (dosyaya yazılır).
DEFAULT_SEED_USERS: dict[str, str] = {
    "admin": "1234",
    "ayse": "1234",
    "hamza": "1234",
    "laperissa": "1234",
}
LOG_COLS = [
    "tarih",
    "kullanici",
    "urun_kodu",
    "degisen_kolon",
    "eski_deger",
    "yeni_deger",
]
TABLE_EDIT_COLS: tuple[str, ...] = (
    COL_URUN_ADI,
    COL_BEDEN,
    COL_PLM,
    COL_RENK,
    COL_ATOLYE,
    COL_KESIM,
    COL_FASON,
    COL_DSM,
    COL_ATOLYE_TERM,
    COL_TAMAMLANDI,
)
# Tabloda loglanacak tüm düzenlenebilir sütunlar (Ürün kodu en sonda; önce diğer alanlar güncellenir).
LOG_EDIT_COLS: tuple[str, ...] = TABLE_EDIT_COLS + (COL_URUN,)
NUMERIC_COLS_KEEP = frozenset({"Kesim Adedi", "Sevk Adedi", "Fire Adedi"})

FASON_OPTIONS = [
    "Hazırlanıyor",
    "Planlanacak",
    "Kesimde",
    "Dikimde",
    "Ütü Paket",
    "Sevk Edildi",
    "Final",
]

FILTER_TERMIN_OPTS: tuple[str, ...] = (
    "Hepsi",
    "Geciken",
    "0-3 gün",
    "4-7 gün",
    "7+ gün",
)
FILTER_FASON_OPTS: tuple[str, ...] = (
    "Hepsi",
    "Kesimde",
    "Dikimde",
    "Ütü Paket",
    "Final",
    "Hazırlanıyor",
)
TRENDYOL_COL_ALIASES: dict[str, tuple[str, ...]] = {
    "urun_kodu": ("ürün kodu", "urun kodu"),
    "plm": ("plm id",),
    "renk": ("renk",),
    "dsm_termin": ("termin tarihi", "termın tarihi"),
    "kesim_adedi": ("toplam po adedi", "toplam poadedi"),
    "fit_durumu": ("fit durumu", "fıt durumu"),
}

def _trendyol_header_key(name: object) -> str:
    s = str(name).strip().replace("\ufeff", "")
    s = " ".join(s.split())
    return s.casefold().replace(" ", "")


def _trendyol_col_excluded_for_dsm(name: str) -> bool:
    ck = _trendyol_header_key(name)
    return any(
        x in ck
        for x in (
            "trendyol",
            "onaylı",
            "onayli",
            "onay",
            "alıcı",
            "alici",
            "depo",
            "urundurumu",
            "uretim",
            "durumuuretim",
        )
    )


def _trendyol_pick_dsm_column(df: pd.DataFrame) -> str | None:
    """TERMİN TARİHİ; TRENDYOL ONAYLI TERMİN hariç."""
    for c in df.columns:
        if _trendyol_col_excluded_for_dsm(str(c)):
            continue
        ck = _trendyol_header_key(c)
        if "termin" in ck and "tarih" in ck:
            return str(c)
    return None


def _trendyol_pick_fit_column(df: pd.DataFrame) -> str | None:
    for c in df.columns:
        ck = _trendyol_header_key(c)
        if "fit" in ck and "durum" in ck:
            return str(c)
    return None


def resolve_trendyol_columns(df: pd.DataFrame) -> dict[str, str | None]:
    """İç alan adı → yapıştırılmış tablodaki gerçek sütun adı."""
    key_to_orig = {_trendyol_header_key(c): str(c) for c in df.columns}
    found: dict[str, str | None] = {}
    for internal, aliases in TRENDYOL_COL_ALIASES.items():
        hit: str | None = None
        for alias in aliases:
            k = _trendyol_header_key(alias)
            if k in key_to_orig:
                hit = key_to_orig[k]
                break
        found[internal] = hit
    if not found.get("dsm_termin"):
        found["dsm_termin"] = _trendyol_pick_dsm_column(df)
    if not found.get("fit_durumu"):
        found["fit_durumu"] = _trendyol_pick_fit_column(df)
    return found


def parse_trendyol_paste_text(text: str) -> pd.DataFrame:
    raw = text.strip()
    if not raw:
        raise ValueError("Yapıştırılan metin boş.")
    parsed = pd.read_csv(StringIO(raw), sep="\t")
    parsed = drop_unnamed_columns(parsed)
    if parsed.empty:
        raise ValueError("Tabloda veri satırı yok.")
    return parsed


def _import_cell_str(row: pd.Series, col: str | None) -> str:
    if not col or col not in row.index:
        return ""
    v = row[col]
    if v is None or v is pd.NA or (isinstance(v, float) and pd.isna(v)):
        return ""
    return str(v).strip()


def _import_dsm_ts(val: object) -> pd.Timestamp | None:
    ts = pd.to_datetime(val, errors="coerce", dayfirst=True)
    if pd.isna(ts):
        return None
    return pd.Timestamp(ts).normalize()


def merge_trendyol_into_base(
    base: pd.DataFrame, paste_df: pd.DataFrame
) -> tuple[pd.DataFrame, int, int]:
    """
    Ürün kodu varsa günceller, yoksa ekler.
    Dönüş: (birleşik_df, yeni_kayıt_sayısı, güncellenen_satır_sayısı)
    """
    cmap = resolve_trendyol_columns(paste_df)
    if not cmap.get("urun_kodu"):
        raise ValueError("Yapıştırılan tabloda 'ÜRÜN KODU' / Ürün Kodu sütunu bulunamadı.")
    out = base.copy().reset_index(drop=True)
    paste_df = paste_df.dropna(how="all").copy()
    ucol = cmap["urun_kodu"]
    paste_df["_code_key"] = paste_df[ucol].map(
        lambda x: _str_norm(x) if pd.notna(x) else ""
    )
    paste_df = paste_df[paste_df["_code_key"] != ""]
    if paste_df.empty:
        raise ValueError("Geçerli ürün kodu içeren satır yok.")
    paste_df = paste_df.drop_duplicates(subset=["_code_key"], keep="last")

    n_new = 0
    n_updated_rows = 0

    for _, row in paste_df.iterrows():
        code = row["_code_key"]
        if not code:
            continue

        mask = out[COL_URUN].astype(str).str.strip() == code
        idxs = out.index[mask].tolist()

        plm = _import_cell_str(row, cmap["plm"])
        renk = _import_cell_str(row, cmap["renk"])
        kesim = 0
        if cmap["kesim_adedi"]:
            kn = pd.to_numeric(row.get(cmap["kesim_adedi"]), errors="coerce")
            kesim = int(kn) if pd.notna(kn) else 0
        dsm_ts: pd.Timestamp | None = None
        if cmap["dsm_termin"]:
            dsm_ts = _import_dsm_ts(row.get(cmap["dsm_termin"]))
        if idxs:
            for ix in idxs:
                if plm:
                    out.at[ix, COL_PLM] = plm
                if renk:
                    out.at[ix, COL_RENK] = renk
                if cmap["kesim_adedi"]:
                    raw_k = row.get(cmap["kesim_adedi"])
                    if raw_k is not None and not (
                        isinstance(raw_k, float) and pd.isna(raw_k)
                    ):
                        if str(raw_k).strip() != "":
                            kn = pd.to_numeric(raw_k, errors="coerce")
                            if pd.notna(kn):
                                out.at[ix, COL_KESIM] = int(kn)
                if dsm_ts is not None:
                    out.at[ix, COL_DSM] = dsm_ts
                n_updated_rows += 1
        else:
            new_row: dict[str, object] = {c: pd.NA for c in out.columns}
            new_row[COL_SB_ID] = pd.NA
            new_row[COL_CREATED] = pd.NaT
            new_row[COL_URUN_ADI] = pd.NA
            new_row[COL_BEDEN] = pd.NA
            new_row[COL_URUN] = code
            new_row[COL_PLM] = plm or pd.NA
            new_row[COL_RENK] = renk or pd.NA
            new_row[COL_KESIM] = kesim
            new_row[COL_ATOLYE] = pd.NA
            new_row[COL_ATOLYE_TERM] = pd.NaT
            new_row[COL_FASON] = "Planlanacak"
            new_row[COL_DSM] = dsm_ts if dsm_ts is not None else pd.NaT
            if COL_TAMAMLANDI in out.columns:
                new_row[COL_TAMAMLANDI] = False
            out = pd.concat(
                [out, pd.DataFrame([new_row], columns=out.columns)],
                ignore_index=True,
            )
            n_new += 1

    return out, n_new, n_updated_rows


def render_trendyol_import_ui(df: pd.DataFrame) -> None:
    if st.session_state.get("_trendyol_clear_paste_next"):
        st.session_state["trendyol_paste_area"] = ""
        st.session_state["_trendyol_clear_paste_next"] = False

    if "trendyol_paste_area" not in st.session_state:
        st.session_state["trendyol_paste_area"] = ""

    if "_trendyol_import_success" in st.session_state:
        eklenen = st.session_state.pop("_trendyol_import_success")
        st.success(f"{eklenen} sipariş eklendi")

    st.caption(
        "Trendyol ekranından tabloyu kopyalayıp (Ctrl+C) aşağıya yapıştırın; "
        "sütunlar sekme (TAB) ile ayrılmış olmalı."
    )
    st.text_area(
        "Trendyol yapıştır",
        height=200,
        key="trendyol_paste_area",
        placeholder="Başlık satırı dahil yapıştırın…",
    )
    if st.button("İçe aktar", type="primary", key="trendyol_import_submit"):
        text = str(st.session_state.get("trendyol_paste_area", "")).strip()
        try:
            pasted = parse_trendyol_paste_text(text)
            base = load_data().copy()
            merged, n_new, n_upd = merge_trendyol_into_base(base, pasted)
            merged = normalize_loaded_df(merged)
            merged = apply_d_ab_t(merged)
            sync_supabase_urunler(base, merged)
            save_veriler_csv_snapshot(merged)
            load_data.clear()
            mark_data_file_saved()
            st.session_state["_trendyol_clear_paste_next"] = True
            st.session_state["_trendyol_import_success"] = n_new
            st.rerun()
        except ValueError as e:
            st.error(str(e))
        except Exception as e:
            st.error(f"Okunamadı: {e}")


def get_log_path() -> Path:
    return Path(__file__).resolve().parent / "log.csv"


def get_veriler_csv_path() -> Path:
    return Path(__file__).resolve().parent / VERILER_CSV


def read_veriler_dataframe() -> pd.DataFrame:
    p = get_veriler_csv_path()
    if not p.exists():
        return pd.DataFrame(columns=list(SB_TO_APP.values()))
    raw = pd.read_csv(p, encoding="utf-8-sig")
    raw = drop_unnamed_columns(raw)
    for _sb, app_col in SB_TO_APP.items():
        if app_col not in raw.columns:
            raw[app_col] = pd.NA
    if COL_SB_ID in raw.columns:
        raw[COL_SB_ID] = pd.to_numeric(raw[COL_SB_ID], errors="coerce").astype("Int64")
    if COL_TAMAMLANDI in raw.columns:
        raw[COL_TAMAMLANDI] = raw[COL_TAMAMLANDI].map(_coerce_bool_loose)
    else:
        raw[COL_TAMAMLANDI] = False
    return raw


def save_veriler_csv_snapshot(df: pd.DataFrame) -> None:
    out = df.drop(
        columns=[c for c in (COL_AUDIT,) if c in df.columns],
        errors="ignore",
    ).copy()
    p = get_veriler_csv_path()
    p.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(p, index=False, encoding="utf-8-sig")


def get_users_csv_path() -> Path:
    return Path(__file__).resolve().parent / USER_FILE


def _must_change_as_bool(val: object) -> bool:
    if val is True or val is False:
        return bool(val)
    if val is None or val is pd.NA:
        return False
    if isinstance(val, float) and pd.isna(val):
        return False
    return str(val).strip().lower() in ("true", "1", "yes")


def load_users() -> pd.DataFrame:
    p = get_users_csv_path()
    if not p.exists():
        df = pd.DataFrame(columns=["username", "password", "must_change"])
        df.to_csv(p, index=False, encoding="utf-8-sig")
    users = pd.read_csv(p, encoding="utf-8-sig")
    for c in ("username", "password", "must_change"):
        if c not in users.columns:
            users[c] = pd.NA if c != "must_change" else False
    if users.empty:
        rows = [
            {
                "username": u.lower(),
                "password": pw,
                "must_change": False,
            }
            for u, pw in DEFAULT_SEED_USERS.items()
        ]
        users = pd.DataFrame(rows)
        save_users(users)
    users["must_change"] = users["must_change"].map(_must_change_as_bool)
    return users


def save_users(df: pd.DataFrame) -> None:
    out = df.copy()
    out.to_csv(get_users_csv_path(), index=False, encoding="utf-8-sig")


def authenticate(username: str, password: str) -> tuple[bool, bool]:
    users = load_users()
    un = str(username).strip().lower()
    user = users[
        (users["username"].astype(str).str.strip().str.lower() == un)
        & (users["password"].astype(str) == str(password))
    ]
    if not user.empty:
        return True, _must_change_as_bool(user.iloc[0]["must_change"])
    return False, False


def change_password(username: str, new_password: str) -> None:
    users = load_users()
    un = str(username).strip().lower()
    mask = users["username"].astype(str).str.strip().str.lower() == un
    if not mask.any():
        return
    users.loc[mask, "password"] = str(new_password)
    users.loc[mask, "must_change"] = False
    save_users(users)


def read_log_df() -> pd.DataFrame:
    p = get_log_path()
    if not p.exists():
        return pd.DataFrame(columns=LOG_COLS)
    d = pd.read_csv(p, encoding="utf-8-sig")
    for c in LOG_COLS:
        if c not in d.columns:
            d[c] = pd.NA
    return d[LOG_COLS]


def append_log_entries(entries: list[dict[str, str]]) -> None:
    if not entries:
        return
    p = get_log_path()
    new_rows = pd.DataFrame(entries)
    for c in LOG_COLS:
        if c not in new_rows.columns:
            new_rows[c] = ""
    new_rows = new_rows[LOG_COLS]
    if p.exists():
        old = read_log_df()
        new_rows = pd.concat([old, new_rows], ignore_index=True)
    p.parent.mkdir(parents=True, exist_ok=True)
    new_rows.to_csv(p, index=False, encoding="utf-8-sig")


def _scalar_for_supabase(app_col: str, val: object) -> object | None:
    if app_col in (COL_DSM, COL_ATOLYE_TERM, COL_CREATED):
        ts = pd.to_datetime(val, errors="coerce")
        if pd.isna(ts):
            return None
        return ts.strftime("%Y-%m-%d")
    if app_col == COL_TAMAMLANDI:
        return bool(_coerce_bool_loose(val))
    if app_col == COL_KESIM:
        n = pd.to_numeric(val, errors="coerce")
        return int(n) if pd.notna(n) else 0
    if val is None or val is pd.NA:
        return None
    if isinstance(val, float) and pd.isna(val):
        return None
    s = str(val).strip()
    return s if s else None


def row_to_supabase_payload(row: pd.Series) -> dict[str, object]:
    payload: dict[str, object] = {}
    for app_c, sb_c in APP_TO_SB.items():
        if app_c == COL_SB_ID:
            continue
        if app_c == COL_CREATED:
            continue
        if app_c not in row.index:
            continue
        payload[sb_c] = _scalar_for_supabase(app_c, row[app_c])
    return payload


def _payload_skip_none(d: dict[str, object]) -> dict[str, object]:
    return {k: v for k, v in d.items() if v is not None}


def insert_row(row_dict: dict[str, object]) -> None:
    supabase.table(SB_TABLE_URUNLER).insert(row_dict).execute()


def sync_supabase_urunler(before: pd.DataFrame, after: pd.DataFrame) -> None:
    """Kayıt öncesi (before) ve sonrası (after) tam tablo; insert/update/delete."""
    b = before.drop(columns=[COL_DAB], errors="ignore").copy()
    a = after.drop(columns=[COL_DAB], errors="ignore").copy()
    for frame in (b, a):
        if COL_SB_ID in frame.columns:
            frame[COL_SB_ID] = pd.to_numeric(
                frame[COL_SB_ID], errors="coerce"
            ).astype("Int64")
    b_ids = {
        int(x)
        for x in b[COL_SB_ID].dropna().tolist()
        if pd.notna(x) and str(x).strip() != ""
    }
    a_ids = {
        int(x)
        for x in a[COL_SB_ID].dropna().tolist()
        if pd.notna(x) and str(x).strip() != ""
    }
    for del_id in b_ids - a_ids:
        supabase.table(SB_TABLE_URUNLER).delete().eq("id", del_id).execute()
    for _, row in a.iterrows():
        rid = row.get(COL_SB_ID)
        raw = row_to_supabase_payload(row)
        if rid is None or pd.isna(rid) or str(rid).strip() == "":
            supabase.table(SB_TABLE_URUNLER).insert(_payload_skip_none(raw)).execute()
        else:
            uid = int(pd.to_numeric(rid, errors="coerce"))
            supabase.table(SB_TABLE_URUNLER).update(raw).eq("id", uid).execute()


def _str_norm(val: object) -> str:
    if val is None or val is pd.NA:
        return ""
    if isinstance(val, float) and pd.isna(val):
        return ""
    return str(val).strip()


def _is_missing_editor_val(val: object, col: str) -> bool:
    if col == COL_TAMAMLANDI:
        return False
    if col in (COL_DSM, COL_ATOLYE_TERM):
        return pd.isna(pd.to_datetime(val, errors="coerce"))
    if col == COL_KESIM:
        return pd.isna(pd.to_numeric(val, errors="coerce"))
    return _str_norm(val) == ""


def _fmt_log_value(val: object) -> str:
    if isinstance(val, bool):
        return "evet" if val else "hayır"
    if val is None or (isinstance(val, float) and pd.isna(val)):
        return ""
    if isinstance(val, pd.Timestamp):
        return val.strftime("%Y-%m-%d")
    if isinstance(val, datetime.datetime):
        return val.strftime("%Y-%m-%d")
    if isinstance(val, datetime.date):
        return val.strftime("%Y-%m-%d")
    ts = pd.to_datetime(val, errors="coerce")
    if pd.notna(ts):
        return ts.strftime("%Y-%m-%d")
    s = str(val).strip()
    return s


def _vals_equal_for_diff(a: object, b: object, col: str) -> bool:
    if col == COL_URUN:
        return _str_norm(a) == _str_norm(b)
    if col == COL_TAMAMLANDI:
        return _coerce_bool_loose(a) == _coerce_bool_loose(b)
    if col in (COL_DSM, COL_ATOLYE_TERM):
        ta = pd.to_datetime(a, errors="coerce")
        tb = pd.to_datetime(b, errors="coerce")
        if pd.isna(ta) and pd.isna(tb):
            return True
        if pd.isna(ta) or pd.isna(tb):
            return False
        return ta.normalize() == tb.normalize()
    if col == COL_KESIM:
        na = pd.to_numeric(a, errors="coerce")
        nb = pd.to_numeric(b, errors="coerce")
        if pd.isna(na) and pd.isna(nb):
            return True
        if pd.isna(na) or pd.isna(nb):
            return False
        return int(na) == int(nb)
    return _str_norm(a) == _str_norm(b)


def audit_summary_for_urun(urun_kodu: str, log_df: pd.DataFrame) -> str:
    if log_df.empty or not str(urun_kodu).strip():
        return ""
    code = str(urun_kodu).strip()
    sub = log_df[log_df["urun_kodu"].astype(str).str.strip() == code]
    if sub.empty:
        return ""
    sub = sub.copy()
    sub["_ts"] = pd.to_datetime(sub["tarih"], errors="coerce", dayfirst=True)
    sub = sub.sort_values("_ts", na_position="first")
    sub = sub.drop_duplicates(subset=["degisen_kolon"], keep="last")
    parts: list[str] = []
    for _, r in sub.iterrows():
        coln = str(r.get("degisen_kolon", "")).strip()
        if coln not in LOG_EDIT_COLS:
            continue
        ku = str(r.get("kullanici", "")).strip()
        ta = str(r.get("tarih", "")).strip()
        parts.append(f"{coln}: {ku} ({ta})")
    return " | ".join(parts)


def prepare_for_data_editor(view: pd.DataFrame) -> pd.DataFrame:
    out = view.copy().reset_index(drop=True)
    log_df = read_log_df()
    out[COL_AUDIT] = out[COL_URUN].map(lambda u: audit_summary_for_urun(str(u), log_df))
    if COL_KESIM in out.columns:
        out[COL_KESIM] = pd.to_numeric(out[COL_KESIM], errors="coerce").astype("Int64")
    for tc in (COL_DSM, COL_ATOLYE_TERM):
        if tc in out.columns:
            out[tc] = pd.to_datetime(out[tc], errors="coerce")
    if COL_DAB in out.columns:
        out[COL_DAB] = pd.to_numeric(out[COL_DAB], errors="coerce").astype("Int64")
    if COL_TAMAMLANDI in out.columns:
        out[COL_TAMAMLANDI] = out[COL_TAMAMLANDI].map(_coerce_bool_loose)
    else:
        out[COL_TAMAMLANDI] = False
    if COL_TAMAMLANDI in out.columns and COL_AUDIT in out.columns:
        others = [c for c in out.columns if c not in (COL_TAMAMLANDI, COL_AUDIT)]
        out = out[others + [COL_TAMAMLANDI, COL_AUDIT]]
    return out


def tablo_gorunumu_excel_df(view: pd.DataFrame, editor_df: pd.DataFrame) -> pd.DataFrame:
    """Tablodaki sütun sırası; D-A=T sayısal; index yok."""
    out = editor_df.copy()
    if COL_DAB in view.columns and COL_DAB in out.columns:
        out[COL_DAB] = pd.to_numeric(view[COL_DAB], errors="coerce").astype("Int64")
    order = [c for c in editor_df.columns if c in out.columns]
    return out[order].reset_index(drop=True)


def to_excel_bytes(df: pd.DataFrame) -> bytes | None:
    buf = BytesIO()
    try:
        df.to_excel(buf, index=False, engine="openpyxl")
    except ImportError:
        return None
    return buf.getvalue()


def tablo_oturum_kullanicisi() -> str:
    u = st.session_state.get("user")
    return str(u).strip() if u else KULLANICI_TABLO


EDITOR_BOOL_COLS: frozenset[str] = frozenset(
    {
        "Fit Onayı",
        "Çizildi",
        COL_TAMAMLANDI,
    }
)

_TR_STATUS_TO_BOOL: dict[str, bool] = {
    "onaylandı": True,
    "onaylanmadı": False,
    "bekliyor": False,
    "çizildi": True,
    "çizilmedi": False,
    "kesildi": True,
    "kesilmedi": False,
    "evet": True,
    "hayır": False,
    "true": True,
    "false": False,
    "1": True,
    "0": False,
    "yes": True,
    "no": False,
}


def _series_to_bool_normalized(s: pd.Series) -> pd.Series:
    out: list[object] = []
    for v in s.tolist():
        if v is None or v is pd.NA:
            out.append(pd.NA)
            continue
        if isinstance(v, bool):
            out.append(v)
            continue
        if isinstance(v, (int, float)) and not isinstance(v, bool):
            if isinstance(v, float) and pd.isna(v):
                out.append(pd.NA)
            elif int(v) == 1:
                out.append(True)
            elif int(v) == 0:
                out.append(False)
            else:
                out.append(pd.NA)
            continue
        k = str(v).strip().casefold()
        if k in _TR_STATUS_TO_BOOL:
            out.append(_TR_STATUS_TO_BOOL[k])
        else:
            out.append(pd.NA)
    return pd.Series(out, index=s.index, dtype="boolean")


def normalize_dataframe_for_streamlit_editor(df: pd.DataFrame) -> pd.DataFrame:
    """st.data_editor / dataframe öncesi: tipleri Streamlit ile uyumlu hale getirir (sütun sırası aynı)."""
    out = df.copy()
    if out.empty:
        return out
    for col in out.columns:
        if col == COL_DAB:
            out[col] = pd.to_numeric(out[col], errors="coerce").astype("Int64")
            continue
        if col in (COL_DSM, COL_ATOLYE_TERM):
            # Tarih sütunlarını string'e çevirmeyip datetime olarak tut ki
            # data_editor'da gerçek tarih sıralaması çalışsın.
            out[col] = pd.to_datetime(out[col], errors="coerce").dt.normalize()
            continue
        cname = str(col)
        if col == COL_CREATED:
            dts = pd.to_datetime(out[col], errors="coerce")
            out[col] = dts.dt.strftime("%Y-%m-%d %H:%M").where(dts.notna(), "")
            continue
        if ("Termin" in cname) or ("Tarih" in cname):
            out[col] = pd.to_datetime(out[col], errors="coerce").dt.normalize()
            continue
        if ("Adet" in cname) or (col == COL_SB_ID):
            out[col] = pd.to_numeric(out[col], errors="coerce")
            if col in (COL_KESIM, COL_SB_ID):
                out[col] = out[col].astype("Int64")
            continue
        if col in EDITOR_BOOL_COLS:
            out[col] = _series_to_bool_normalized(out[col])
            continue
        s = out[col].astype(str)
        out[col] = s.replace(
            to_replace=r"^(nan|NaT|None|<NA>)$", value="", regex=True
        )
    return out


def _resolve_row_ix(
    ix_by_code: dict[str, int], orig_key: str, code_now: str
) -> int | None:
    o = str(orig_key).strip() if orig_key else ""
    c = str(code_now).strip() if code_now else ""
    if o and o in ix_by_code:
        return ix_by_code[o]
    if c and c in ix_by_code:
        return ix_by_code[c]
    return None


def _log_line(
    kullanici: str,
    now: str,
    urun_ctx: str,
    col: str,
    eski: str,
    yeni: str,
) -> dict[str, str]:
    return {
        "tarih": now,
        "kullanici": kullanici,
        "urun_kodu": urun_ctx,
        "degisen_kolon": col,
        "eski_deger": eski,
        "yeni_deger": yeni,
    }


def apply_table_save(
    full_before: pd.DataFrame,
    edited: pd.DataFrame,
    kullanici: str,
    *,
    editor_row_urun_keys: list[str] | None = None,
) -> tuple[pd.DataFrame, list[dict[str, str]]]:
    """Tam veri kümesini günceller; her hücre değişiminde kullanıcı, tarih-saat, eski/yeni değer log.csv’ye yazılır."""
    log_entries: list[dict[str, str]] = []
    edit_df = edited.drop(
        columns=[c for c in (COL_AUDIT,) if c in edited.columns],
        errors="ignore",
    ).copy()
    if COL_URUN not in edit_df.columns:
        return full_before, log_entries
    edit_df[COL_URUN] = edit_df[COL_URUN].astype(str).str.strip()
    edit_df = edit_df[edit_df[COL_URUN] != ""]
    if edit_df.empty:
        return full_before, log_entries
    dup = edit_df[COL_URUN].duplicated()
    if dup.any():
        raise ValueError("Tabloda aynı ürün kodundan birden fazla satır var.")
    full = full_before.copy().reset_index(drop=True)
    ix_by_code = {
        str(r[COL_URUN]).strip(): i
        for i, r in full.iterrows()
        if str(r[COL_URUN]).strip()
    }
    now = datetime.datetime.now().replace(microsecond=0).strftime("%d.%m.%Y %H:%M:%S")
    keys = editor_row_urun_keys or []
    for row_i, (_, er) in enumerate(edit_df.iterrows()):
        code_now = str(er[COL_URUN]).strip()
        orig_key = str(keys[row_i]).strip() if row_i < len(keys) else ""
        ri = _resolve_row_ix(ix_by_code, orig_key, code_now)
        if ri is None:
            new_row: dict[str, object] = {c: pd.NA for c in full.columns}
            for c in full.columns:
                if c == COL_DAB:
                    continue
                if c in er.index:
                    new_row[c] = er.get(c)
            if COL_TAMAMLANDI in full.columns:
                new_row[COL_TAMAMLANDI] = _coerce_bool_loose(
                    new_row.get(COL_TAMAMLANDI)
                )
            for col in LOG_EDIT_COLS:
                if col not in full.columns:
                    continue
                nv = er.get(col)
                if _is_missing_editor_val(nv, col):
                    continue
                log_entries.append(
                    _log_line(
                        kullanici,
                        now,
                        code_now,
                        col,
                        "",
                        _fmt_log_value(nv),
                    )
                )
            full = pd.concat(
                [full, pd.DataFrame([new_row], columns=full.columns)],
                ignore_index=True,
            )
            ix_by_code[code_now] = len(full) - 1
            continue
        prev_urun = str(full.at[ri, COL_URUN]).strip()
        for col in LOG_EDIT_COLS:
            if col not in full.columns or col not in er.index:
                continue
            old_v = full.at[ri, col]
            new_v = er[col]
            if _is_missing_editor_val(new_v, col) and col != COL_URUN:
                continue
            if _vals_equal_for_diff(old_v, new_v, col):
                continue
            if col == COL_URUN:
                nu = _str_norm(new_v)
                if nu and nu != prev_urun and nu in ix_by_code and ix_by_code[nu] != ri:
                    raise ValueError(f"'{nu}' ürün kodu zaten kullanılıyor.")
            log_entries.append(
                _log_line(
                    kullanici,
                    now,
                    prev_urun,
                    col,
                    _fmt_log_value(old_v),
                    _fmt_log_value(new_v),
                )
            )
            full.at[ri, col] = new_v
            if col == COL_URUN:
                nu2 = _str_norm(new_v)
                if prev_urun and prev_urun in ix_by_code:
                    del ix_by_code[prev_urun]
                if nu2:
                    ix_by_code[nu2] = ri
                prev_urun = nu2
    full = normalize_loaded_df(full)
    full = apply_d_ab_t(full)
    return full, log_entries


def get_atolyeler_csv_path() -> Path:
    return Path(__file__).resolve().parent / "atolyeler.csv"


def dedupe_atolye_names(names: list[str]) -> list[str]:
    seen: dict[str, str] = {}
    for n in names:
        s = str(n).strip()
        if not s:
            continue
        k = s.casefold()
        if k not in seen:
            seen[k] = s
    return sorted(seen.values(), key=lambda x: x.casefold())


def read_atolyeler_list() -> list[str]:
    p = get_atolyeler_csv_path()
    if not p.exists():
        return []
    d = pd.read_csv(p, encoding="utf-8-sig")
    if d.empty:
        return []
    col = d.columns[0]
    return dedupe_atolye_names(d[col].dropna().astype(str).tolist())


def merge_atolye_sources(df: pd.DataFrame) -> list[str]:
    from_df = df[COL_ATOLYE].dropna().astype(str).str.strip().tolist()
    return dedupe_atolye_names(from_df + read_atolyeler_list())


def write_atolyeler_csv(names: list[str]) -> None:
    uniq = dedupe_atolye_names(names)
    get_atolyeler_csv_path().parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame({COL_ATOLYE: uniq}).to_csv(
        get_atolyeler_csv_path(), index=False, encoding="utf-8-sig"
    )


def register_atolye(name: str, df: pd.DataFrame) -> str:
    s = str(name).strip()
    if not s:
        return ""
    merged = merge_atolye_sources(df)
    for m in merged:
        if m.casefold() == s.casefold():
            return m
    combined = read_atolyeler_list() + [s]
    write_atolyeler_csv(combined)
    return s


def ensure_last_save_bootstrap() -> None:
    if "_last_save_at" not in st.session_state:
        st.session_state["_last_save_at"] = datetime.datetime.now().replace(
            microsecond=0
        )


def mark_data_file_saved() -> None:
    st.session_state["_last_save_at"] = datetime.datetime.now().replace(microsecond=0)


def persist_table_edits(edited_df: object, *, toast_message: str | None) -> bool:
    try:
        if isinstance(edited_df, dict):
            if "data" in edited_df:
                edited_df = pd.DataFrame(edited_df["data"])
            else:
                st.session_state["_autosave_err"] = "Tablo verisi okunamadı (dict, data yok)."
                return False
        if not hasattr(edited_df, "columns"):
            st.session_state["_autosave_err"] = "Tablo verisi okunamadı (DataFrame değil)."
            return False
        full_before = load_data()
        row_keys = st.session_state.get("_editor_row_urun_keys")
        if not isinstance(row_keys, list):
            row_keys = None
        out_df, log_rows = apply_table_save(
            full_before,
            edited_df,
            tablo_oturum_kullanicisi(),
            editor_row_urun_keys=row_keys,
        )
        ec = edited_df.drop(
            columns=[c for c in (COL_AUDIT,) if c in edited_df.columns],
            errors="ignore",
        )
        for _, er in ec.iterrows():
            av = _str_norm(er.get(COL_ATOLYE))
            if av:
                register_atolye(av, out_df)
        append_log_entries(log_rows)
        sync_supabase_urunler(full_before, out_df)
        save_veriler_csv_snapshot(out_df)
        load_data.clear()
        mark_data_file_saved()
        st.session_state.pop("_autosave_err", None)
        if toast_message:
            icon = "💾" if toast_message.startswith("Otomatik") else "✅"
            st.toast(toast_message, icon=icon)
        return True
    except ValueError as err:
        st.session_state["_autosave_err"] = str(err)
        return False


def apply_d_ab_t(df: pd.DataFrame) -> pd.DataFrame:
    """Terminleri temizler, D-A=T hesaplar, aşırı geçmiş değerleri boşaltır, sıralar."""
    df = df.copy()
    if COL_DSM in df.columns:
        df[COL_DSM] = pd.to_datetime(df[COL_DSM], errors="coerce")
    if COL_ATOLYE_TERM in df.columns:
        df[COL_ATOLYE_TERM] = pd.to_datetime(df[COL_ATOLYE_TERM], errors="coerce")
    at = (
        df[COL_ATOLYE_TERM]
        if COL_ATOLYE_TERM in df.columns
        else pd.Series(pd.NaT, index=df.index)
    )
    dsm = df[COL_DSM] if COL_DSM in df.columns else pd.Series(pd.NaT, index=df.index)
    termin_kolon = at.combine_first(dsm)
    bugun = pd.Timestamp.today().normalize()
    df[COL_DAB] = (termin_kolon - bugun).dt.days
    df.loc[df[COL_DAB].notna() & (df[COL_DAB] < -60), COL_DAB] = pd.NA
    df[COL_DAB] = df[COL_DAB].astype("Int64")
    return df.sort_values(COL_DAB, ascending=True, na_position="last")


def normalize_loaded_df(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.convert_dtypes()
    for tc in (COL_DSM, COL_ATOLYE_TERM, COL_CREATED):
        if tc in df.columns:
            df[tc] = pd.to_datetime(df[tc], errors="coerce")
    for col in df.columns:
        c = str(col)
        if "Termin" in c or "Tarih" in c or c == COL_CREATED:
            df[col] = pd.to_datetime(df[col], errors="coerce")
    if COL_TAMAMLANDI in df.columns:
        df[COL_TAMAMLANDI] = df[COL_TAMAMLANDI].map(_coerce_bool_loose)
    else:
        df[COL_TAMAMLANDI] = False
    return df


@st.cache_data(ttl=30, show_spinner="Veri yükleniyor…")
def load_data() -> pd.DataFrame:
    raw = read_veriler_dataframe()
    df = normalize_loaded_df(raw)
    return apply_d_ab_t(df)


def drop_unnamed_columns(df: pd.DataFrame) -> pd.DataFrame:
    keep = [c for c in df.columns if not str(c).startswith("Unnamed")]
    return df[keep]


def prepare_for_display(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    for col in out.select_dtypes(include=["datetime64[ns]"]).columns:
        s = out[col]
        out[col] = s.dt.strftime("%d.%m.%Y").where(s.notna(), "")
    for col in out.columns:
        if pd.api.types.is_datetime64_any_dtype(out[col]):
            s = out[col]
            out[col] = s.dt.strftime("%d.%m.%Y").where(s.notna(), "")
    for col in out.columns:
        if col not in NUMERIC_COLS_KEEP:
            out[col] = out[col].astype(object)
    return out


def sort_by_dab_asc(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    sort_cols: list[str] = []
    ascending: list[bool] = []
    if COL_DSM in out.columns:
        out[COL_DSM] = pd.to_datetime(out[COL_DSM], errors="coerce")
        sort_cols.append(COL_DSM)
        ascending.append(True)
    if COL_DAB in out.columns:
        out[COL_DAB] = pd.to_numeric(out[COL_DAB], errors="coerce")
        sort_cols.append(COL_DAB)
        ascending.append(True)
    if not sort_cols:
        return out
    return out.sort_values(sort_cols, ascending=ascending, na_position="last")


def count_geciken_yaklasan(df: pd.DataFrame) -> tuple[int, int]:
    dab = pd.to_numeric(df[COL_DAB], errors="coerce")
    geciken = int((dab < 0).sum())
    yaklasan = int(((dab >= 0) & (dab <= 3)).sum())
    return geciken, yaklasan


def canonical_fason_for_filter(val: object) -> str | None:
    """CSV’deki varyantları (Dikim’de, Ütü Paket’de vb.) filtre seçenekleriyle eşler."""
    if val is None or val is pd.NA:
        return None
    if isinstance(val, float) and pd.isna(val):
        return None
    s = str(val).strip()
    if not s or s == "-":
        return None
    cf = s.casefold().replace("'", "").replace("’", "")
    cf_ns = "".join(cf.split())
    if "final" in cf:
        return "Final"
    if "hazırlanıyor" in cf or "hazirlaniyor" in cf_ns:
        return "Hazırlanıyor"
    if "ütü" in cf and "paket" in cf:
        return "Ütü Paket"
    if "dikim" in cf:
        return "Dikimde"
    if "kesim" in cf:
        return "Kesimde"
    return None


def mask_termin_durum_filter(df: pd.DataFrame, choice: str) -> pd.Series:
    if choice == "Hepsi" or COL_DAB not in df.columns:
        return pd.Series(True, index=df.index)
    dab = pd.to_numeric(df[COL_DAB], errors="coerce")
    if choice == "Geciken":
        return dab.notna() & (dab < 0)
    if choice == "0-3 gün":
        return dab.notna() & (dab >= 0) & (dab <= 3)
    if choice == "4-7 gün":
        return dab.notna() & (dab >= 4) & (dab <= 7)
    if choice == "7+ gün":
        return dab.notna() & (dab > 7)
    return pd.Series(True, index=df.index)


def mask_fason_filter(df: pd.DataFrame, choice: str) -> pd.Series:
    if choice == "Hepsi" or COL_FASON not in df.columns:
        return pd.Series(True, index=df.index)
    ch = str(choice).strip()

    def _fason_cell_matches(val: object) -> bool:
        if canonical_fason_for_filter(val) == ch:
            return True
        s = _str_norm(val)
        if not s:
            return False
        return s.casefold() == ch.casefold()

    return df[COL_FASON].map(_fason_cell_matches)


GLOBAL_SEARCH_COLS: tuple[str, ...] = (
    COL_URUN,
    COL_URUN_ADI,
    COL_BEDEN,
    COL_PLM,
    COL_RENK,
    COL_ATOLYE,
    COL_FASON,
)


def mask_global_text_search(df: pd.DataFrame, query: str) -> pd.Series:
    q = str(query).strip().casefold()
    if not q:
        return pd.Series(True, index=df.index)
    parts: list[pd.Series] = []
    for c in GLOBAL_SEARCH_COLS:
        if c not in df.columns:
            continue
        hay = df[c].map(lambda x: "" if pd.isna(x) else str(x).strip().casefold())
        parts.append(hay.str.contains(q, regex=False, na=False))
    if not parts:
        return pd.Series(True, index=df.index)
    m = parts[0]
    for p in parts[1:]:
        m = m | p
    return m


def style_by_dab(df: pd.DataFrame) -> pd.io.formats.style.Styler:
    def row_style(row: pd.Series) -> list[str]:
        n = len(row)
        empty = [""] * n
        if COL_DAB not in row.index:
            return empty
        v = pd.to_numeric(row[COL_DAB], errors="coerce")
        if pd.isna(v):
            return empty
        if v < 0:
            return ["background-color: #fecaca; color: #450a0a;"] * n
        if 0 <= v <= 3:
            return ["background-color: #fef08a; color: #422006;"] * n
        return empty

    return df.style.apply(row_style, axis=1)


def _cell_str(val: object) -> str:
    if val is None or (isinstance(val, float) and pd.isna(val)):
        return ""
    return str(val)


def _cell_date(val: object) -> datetime.date:
    ts = pd.to_datetime(val, errors="coerce")
    if pd.isna(ts):
        return datetime.date.today()
    return ts.date()


def _existing_urun_codes(df: pd.DataFrame) -> set[str]:
    return set(df[COL_URUN].dropna().astype(str).str.strip())


def sync_form_new_defaults(df: pd.DataFrame, code: str) -> None:
    ats = merge_atolye_sources(df)
    today = datetime.date.today()
    st.session_state["form_i_urun"] = str(code).strip()
    st.session_state["form_i_plm"] = ""
    st.session_state["form_i_renk"] = ""
    st.session_state["form_i_kesim"] = 0
    st.session_state["form_i_urun_adi"] = ""
    st.session_state["form_i_beden"] = ""
    st.session_state["form_i_fason"] = FASON_OPTIONS[0]
    st.session_state["form_i_atolye"] = ats[0] if ats else ""
    st.session_state["form_dsm"] = today
    st.session_state["form_atolye_term"] = today


def sync_form_load_existing(df: pd.DataFrame, pick: str) -> None:
    merged_at = merge_atolye_sources(df)
    m = df[df[COL_URUN].astype(str) == str(pick).strip()]
    if m.empty:
        return
    r = m.iloc[0]
    st.session_state["form_i_urun"] = _cell_str(r.get(COL_URUN))
    st.session_state["form_i_plm"] = _cell_str(r.get(COL_PLM))
    st.session_state["form_i_renk"] = _cell_str(r.get(COL_RENK))
    kn = pd.to_numeric(r.get(COL_KESIM), errors="coerce")
    st.session_state["form_i_kesim"] = int(kn) if pd.notna(kn) else 0
    st.session_state["form_i_urun_adi"] = _cell_str(r.get(COL_URUN_ADI))
    st.session_state["form_i_beden"] = _cell_str(r.get(COL_BEDEN))
    fv = _cell_str(r.get(COL_FASON))
    st.session_state["form_i_fason"] = fv if fv in FASON_OPTIONS else FASON_OPTIONS[0]
    av = _cell_str(r.get(COL_ATOLYE))
    if av:
        canon = next(
            (x for x in merged_at if x.casefold() == av.casefold()),
            av,
        )
        st.session_state["form_i_atolye"] = canon
    else:
        st.session_state["form_i_atolye"] = merged_at[0] if merged_at else ""
    st.session_state["form_dsm"] = _cell_date(r.get(COL_DSM))
    st.session_state["form_atolye_term"] = _cell_date(r.get(COL_ATOLYE_TERM))


def apply_urun_sync() -> None:
    df = load_data()
    ex = _existing_urun_codes(df)
    cur = str(st.session_state.get("form_i_urun", "")).strip()
    prev = str(st.session_state.get("_urun_prev_value", "")).strip()
    if prev in ex and cur != prev:
        st.session_state["_rename_from"] = prev
    if not cur:
        st.session_state["_urun_prev_value"] = ""
        return
    if cur in ex:
        sync_form_load_existing(df, cur)
    elif prev in ex and cur not in ex:
        sync_form_new_defaults(df, cur)
    st.session_state["_urun_prev_value"] = cur


def on_urun_quick_pick() -> None:
    v = st.session_state.get("urun_quick")
    if not v or v == "—":
        return
    st.session_state["form_i_urun"] = v
    st.session_state["urun_quick"] = "—"
    apply_urun_sync()


def on_atolye_quick_pick() -> None:
    v = st.session_state.get("atolye_quick")
    if not v or v == "—":
        return
    st.session_state["form_i_atolye"] = v
    st.session_state["atolye_quick"] = "—"


def build_row_dict(
    df: pd.DataFrame,
    form: dict[str, object],
    *,
    existing: pd.Series | None = None,
) -> dict[str, object]:
    row: dict[str, object] = {c: pd.NA for c in df.columns}
    if existing is not None and COL_SB_ID in existing.index:
        row[COL_SB_ID] = existing.get(COL_SB_ID)
    else:
        row[COL_SB_ID] = pd.NA
    if existing is not None and COL_CREATED in existing.index:
        row[COL_CREATED] = existing.get(COL_CREATED)
    else:
        row[COL_CREATED] = pd.NaT
    row[COL_URUN] = str(form["urun_kodu"]).strip()
    ua = str(form.get("urun_adi", "")).strip()
    row[COL_URUN_ADI] = ua or pd.NA
    bd = str(form.get("beden", "")).strip()
    row[COL_BEDEN] = bd or pd.NA
    row[COL_PLM] = str(form["plm"]).strip() or pd.NA
    row[COL_RENK] = str(form["renk"]).strip() or pd.NA
    row[COL_ATOLYE] = str(form["atolye"]).strip() or pd.NA
    row[COL_KESIM] = int(form["kesim_adedi"])
    row[COL_FASON] = str(form["fason_durum"])
    row[COL_DSM] = pd.Timestamp(form["dsm_termin"])
    row[COL_ATOLYE_TERM] = pd.Timestamp(form["atolye_termin"])
    if COL_TAMAMLANDI in df.columns:
        if existing is not None and COL_TAMAMLANDI in existing.index:
            row[COL_TAMAMLANDI] = _coerce_bool_loose(existing.get(COL_TAMAMLANDI))
        else:
            row[COL_TAMAMLANDI] = False
    return row


def render_urun_kayit_form(df: pd.DataFrame) -> None:
    st.markdown("**Yeni ürün veya mevcut kodu güncelleme**")
    urun_codes_sorted = sorted(df[COL_URUN].dropna().astype(str).unique().tolist())
    st.text_input(
        "Ürün kodu",
        key="form_i_urun",
        placeholder="TBBSS26AI00045 gibi bir kod girin",
        on_change=apply_urun_sync,
    )
    st.caption("Mevcut kodlardan seçin:")
    st.selectbox(
        "Mevcut kodlardan seç",
        ["—"] + urun_codes_sorted,
        key="urun_quick",
        on_change=on_urun_quick_pick,
        label_visibility="collapsed",
    )
    atolye_suggestions = merge_atolye_sources(df)
    st.text_input(
        "Atölye",
        key="form_i_atolye",
        placeholder="Atölye adı yazın veya alttaki öneriden seçin",
    )
    st.caption("Mevcut atölyelerden seçin:")
    st.selectbox(
        "Atölye önerisi",
        ["—"] + atolye_suggestions,
        key="atolye_quick",
        on_change=on_atolye_quick_pick,
        label_visibility="collapsed",
    )
    with st.form("urun_kayit_form"):
        st.text_input("Ürün adı", key="form_i_urun_adi")
        st.text_input("Beden", key="form_i_beden")
        st.text_input("PLM", key="form_i_plm")
        st.text_input("Renk", key="form_i_renk")
        st.number_input("Kesim Adedi", min_value=0, step=1, key="form_i_kesim")
        st.selectbox("Fason Durum", FASON_OPTIONS, key="form_i_fason")
        st.date_input("DSM Termin", key="form_dsm")
        st.date_input("Atölye Termin", key="form_atolye_term")
        submitted = st.form_submit_button("Kaydet")
    if submitted:
        urun_kodu_val = str(st.session_state.get("form_i_urun", "")).strip()
        if not urun_kodu_val:
            st.error("Ürün kodu zorunludur.")
        else:
            form_vals = {
                "urun_kodu": urun_kodu_val,
                "urun_adi": st.session_state.get("form_i_urun_adi", ""),
                "beden": st.session_state.get("form_i_beden", ""),
                "plm": st.session_state.get("form_i_plm", ""),
                "renk": st.session_state.get("form_i_renk", ""),
                "atolye": st.session_state.get("form_i_atolye", ""),
                "kesim_adedi": st.session_state.get("form_i_kesim", 0),
                "fason_durum": st.session_state.get("form_i_fason", FASON_OPTIONS[0]),
                "dsm_termin": st.session_state.get("form_dsm"),
                "atolye_termin": st.session_state.get("form_atolye_term"),
            }
            base = load_data().copy()
            canon_at = register_atolye(str(form_vals.get("atolye", "")), base)
            form_vals["atolye"] = canon_at
            code = str(form_vals["urun_kodu"]).strip()
            dup_mask = base[COL_URUN].astype(str) == code
            if dup_mask.sum() > 1:
                st.error(
                    "Bu ürün kodu için birden fazla satır var; önce veriyi düzeltin."
                )
            else:
                full_before = base.copy()
                existing_row = (
                    base.loc[dup_mask].iloc[0] if bool(dup_mask.any()) else None
                )
                base = base[~dup_mask]
                rf = st.session_state.get("_rename_from")
                if rf and str(rf).strip() and str(rf).strip() != code:
                    base = base[base[COL_URUN].astype(str) != str(rf).strip()]
                new_row = build_row_dict(base, form_vals, existing=existing_row)
                new_df = pd.DataFrame([new_row], columns=base.columns)
                out_df = pd.concat([base, new_df], ignore_index=True)
                out_df = normalize_loaded_df(out_df)
                out_df = apply_d_ab_t(out_df)
                sync_supabase_urunler(full_before, out_df)
                save_veriler_csv_snapshot(out_df)
                load_data.clear()
                mark_data_file_saved()
                st.session_state["_rename_from"] = None
                st.session_state["_urun_prev_value"] = code
                st.toast("Kayıt kaydedildi.", icon="✅")
                st.rerun()


def _inject_layout_css() -> None:
    st.markdown(
        """
        <style>
            [data-testid="stMetricContainer"] {
                padding: 0.35rem 0.5rem;
                background: #f8fafc;
                border-radius: 8px;
                border: 1px solid #e2e8f0;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_login_screen() -> None:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("login_form"):
            st.markdown(
                '<img src="https://raw.githubusercontent.com/fovalioglu/urun-takip-sistemi/main/logo.png" class="login-logo">',
                unsafe_allow_html=True,
            )
            st.text_input("Kullanıcı adı", key="login_username")
            st.text_input("Şifre", type="password", key="login_password")
            submitted = st.form_submit_button("Giriş", use_container_width=True)
    if submitted:
        u = str(st.session_state.get("login_username", "")).strip()
        p = str(st.session_state.get("login_password", ""))
        ok, must_ch = authenticate(u, p)
        if ok:
            st.session_state.logged_in = True
            st.session_state["user"] = u.strip().lower()
            st.session_state["must_change_password"] = bool(must_ch)
            st.rerun()
        else:
            ec1, ec2, ec3 = st.columns([1, 2, 1])
            with ec2:
                st.error("kullanıcı adı veya şifre yanlış")


def render_force_password_change() -> None:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.markdown(
            "<p style='text-align:center;color:#111827;font-weight:500;margin-bottom:1rem;'>"
            "Güvenlik için yeni bir şifre belirlemeniz gerekiyor.</p>",
            unsafe_allow_html=True,
        )
        with st.form("force_password_change_form"):
            st.text_input("Yeni şifre", type="password", key="force_pw_new")
            st.text_input("Yeni şifre (tekrar)", type="password", key="force_pw_new2")
            sub = st.form_submit_button("Şifreyi kaydet", use_container_width=True)
    if sub:
        n1 = str(st.session_state.get("force_pw_new", ""))
        n2 = str(st.session_state.get("force_pw_new2", ""))
        ec1, ec2, ec3 = st.columns([1, 2, 1])
        with ec2:
            if len(n1) < 4:
                st.error("Şifre en az 4 karakter olmalı.")
            elif n1 != n2:
                st.error("Şifreler eşleşmiyor.")
            else:
                change_password(str(st.session_state.get("user", "")), n1)
                st.session_state["must_change_password"] = False
                st.rerun()


_inject_layout_css()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    render_login_screen()
    st.stop()

if st.session_state.get("must_change_password"):
    render_force_password_change()
    st.stop()

try:
    df = load_data()
except FileNotFoundError as e:
    st.error(str(e))
    st.stop()

if COL_ATOLYE not in df.columns or COL_URUN not in df.columns:
    st.error(
        "Veride 'Atölye' veya 'Ürün Kodu' sütunu bulunamadı. "
        f"Mevcut sütunlar: {', '.join(map(str, df.columns))}"
    )
    st.stop()

ensure_last_save_bootstrap()

title_col, action_col = st.columns([4, 2], gap="small")
with title_col:
    st.markdown(
        """
<div style="
display:flex;
align-items:center;
gap:12px;
margin-bottom:5px;
">

<img src="https://raw.githubusercontent.com/fovalioglu/urun-takip-sistemi/main/logo.png"
style="
height:42px;
object-fit:contain;
">

</div>
""",
        unsafe_allow_html=True,
    )
    st.caption("Termin ve atölye takibi")
    st.markdown(
        """
<style>

h1{
display:none;
}

</style>
""",
        unsafe_allow_html=True,
    )
with action_col:
    _u = html.escape(str(st.session_state.get("user", "")))
    _ur, _on, _lo = st.columns([1.35, 1.05, 0.72], gap="small")
    with _ur:
        st.markdown(
            f'<div style="text-align:right;font-size:0.9rem;color:#111827;font-weight:500;'
            f'margin:0 0 0.35rem 0;line-height:2rem;">{_u}</div>',
            unsafe_allow_html=True,
        )
    with _on:
        render_online_users()
    with _lo:
        if st.button("Çıkış", key="btn_logout", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.pop("user", None)
            st.session_state.pop("must_change_password", None)
            st.rerun()
    _ls = st.session_state.get("_last_save_at")
    _hm = _ls.strftime("%H:%M") if isinstance(_ls, datetime.datetime) else "—"
    st.markdown(
        f'<div style="text-align:right;font-size:0.75rem;color:#111827;font-weight:500;'
        f'margin:0 0 0.35rem 0;">son kayıt: {_hm}</div>',
        unsafe_allow_html=True,
    )
    a1, a2 = st.columns(2, gap="small")
    with a1:
        if hasattr(st, "popover"):
            with st.popover("➕ Yeni Ürün", use_container_width=True, width="stretch"):
                render_urun_kayit_form(df)
        else:
            if st.button("➕ Yeni Ürün", use_container_width=True, key="btn_open_form"):
                st.session_state["_urun_form_expanded"] = True
    with a2:
        if hasattr(st, "popover"):
            with st.popover(
                "Siparişleri İçeri Aktar",
                use_container_width=True,
                width="stretch",
            ):
                render_trendyol_import_ui(df)
        else:
            with st.expander("Siparişleri İçeri Aktar", expanded=False):
                render_trendyol_import_ui(df)

if not hasattr(st, "popover") and st.session_state.get("_urun_form_expanded"):
    with st.expander("Ürün kayıt formu", expanded=True):
        render_urun_kayit_form(df)
        if st.button("Kapat", key="btn_close_form"):
            st.session_state["_urun_form_expanded"] = False
            st.rerun()

atolye_opts = merge_atolye_sources(df)
urun_opts = sorted(df[COL_URUN].dropna().astype(str).unique().tolist())

flt_a, flt_u, flt_t, flt_f, flt_done = st.columns([1, 1, 1, 1, 1.05], gap="small")
with flt_a:
    atolye_filter = st.selectbox(
        "Atölye",
        ["Tümü"] + atolye_opts,
        key="f_atolye",
    )
with flt_u:
    urun_filter = st.selectbox(
        "Ürün Kodu",
        ["Tümü"] + urun_opts,
        key="f_urun",
    )
with flt_t:
    termin_filter = st.selectbox(
        "Termin Durumu",
        FILTER_TERMIN_OPTS,
        key="f_termin",
    )
with flt_f:
    fason_filter = st.selectbox(
        "Fason Durum",
        FILTER_FASON_OPTS,
        key="f_fason",
    )
with flt_done:
    show_completed = st.checkbox(
        "Tamamlananları Göster",
        value=False,
        key="f_show_completed",
        help="Kapalıyken yalnızca henüz tamamlanmamış kayıtlar listelenir.",
    )

filtered_df = df.copy()
if atolye_filter != "Tümü":
    af = str(atolye_filter).strip().casefold()
    filtered_df = filtered_df[
        filtered_df[COL_ATOLYE].astype(str).str.strip().str.casefold() == af
    ]
if urun_filter != "Tümü":
    filtered_df = filtered_df[filtered_df[COL_URUN].astype(str) == urun_filter]

if termin_filter != "Hepsi":
    filtered_df = filtered_df.loc[
        mask_termin_durum_filter(filtered_df, termin_filter)
    ]
if fason_filter != "Hepsi":
    filtered_df = filtered_df.loc[mask_fason_filter(filtered_df, fason_filter)]

search_q = st.text_input(
    "Genel arama",
    key="f_global_search",
    placeholder="Ürün kodu, adı, beden, PLM, renk, atölye, fason…",
    help=(
        "Yazdığınız metin bu sütunlardan en az birinde geçen satırları gösterir "
        "(büyük/küçük harf duyarsız, kısmi eşleşme). Her yeniden çalıştırmada uygulanır."
    ),
)
filtered_df = filtered_df.loc[mask_global_text_search(filtered_df, search_q)]

if (
    not show_completed
    and COL_TAMAMLANDI in filtered_df.columns
    and not filtered_df.empty
):
    _tam_done = filtered_df[COL_TAMAMLANDI].map(_coerce_bool_loose)
    filtered_df = filtered_df.loc[~_tam_done]

view = sort_by_dab_asc(filtered_df)
view = drop_unnamed_columns(view)
view = view.reset_index(drop=True)
editor_full = prepare_for_data_editor(view)

geciken, yaklasan = count_geciken_yaklasan(filtered_df)
m1, m2, m3 = st.columns([1, 1, 1.35], gap="small")
with m1:
    st.metric("Geciken (D-A=T < 0)", geciken)
with m2:
    st.metric("Yaklaşan (0–3 gün)", yaklasan)
with m3:
    _cap = (
        f"**Genel filtre sonrası:** {len(view)} satır · **Toplam veri:** {len(df)} satır"
    )
    if (
        show_completed
        and COL_TAMAMLANDI in filtered_df.columns
        and not filtered_df.empty
    ):
        _ndone = int(filtered_df[COL_TAMAMLANDI].map(_coerce_bool_loose).sum())
        _cap += f" · **Tamamlanan (bu liste):** {_ndone}"
    st.caption(_cap)

editor_df = normalize_dataframe_for_streamlit_editor(editor_full.copy())
view_for_excel = view.copy()
excel_export_df = tablo_gorunumu_excel_df(view_for_excel, editor_df)

df_display = editor_df.copy()
if len(df_display) > 100:
    df_display = df_display.iloc[:100]

_dl1, _dl2 = st.columns([2, 1], gap="small")
with _dl1:
    if len(editor_df) > 100:
        st.caption(
            f"**Gösterilen:** ilk 100 satır (filtre sonrası toplam {len(editor_df)} satır)"
        )
    else:
        st.caption(f"**Gösterilen:** {len(df_display)} satır")
with _dl2:
    _xlsx = to_excel_bytes(excel_export_df)
    if _xlsx is None:
        st.caption("Excel için: `pip install openpyxl`")
    else:
        st.download_button(
            label="📥 Excel indir",
            data=_xlsx,
            file_name="urun_takip.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            key="dl_tablo_excel",
            use_container_width=True,
        )

if COL_URUN in df_display.columns:
    st.session_state["_editor_row_urun_keys"] = (
        df_display[COL_URUN].astype(str).str.strip().tolist()
    )
else:
    st.session_state.pop("_editor_row_urun_keys", None)

_colcfg: dict = {}
if COL_TAMAMLANDI in df_display.columns:
    _colcfg[COL_TAMAMLANDI] = st.column_config.CheckboxColumn(
        COL_TAMAMLANDI,
        help="İşaretleyince kayıt tamamlanır ve veritabanına kaydedilir; "
        "ana listede varsayılan olarak gizlenir.",
        default=False,
    )
if COL_DSM in df_display.columns:
    _colcfg[COL_DSM] = st.column_config.DateColumn(COL_DSM, format="YYYY-MM-DD")
if COL_DAB in df_display.columns:
    _colcfg[COL_DAB] = st.column_config.NumberColumn(COL_DAB, format="%d")
_de_kwargs: dict = {
    "height": 700,
    "use_container_width": True,
    "hide_index": True,
    "num_rows": "fixed",
    "key": "main_table",
}
if _colcfg:
    _de_kwargs["column_config"] = _colcfg
_edited_raw = st.data_editor(df_display, **_de_kwargs)

if show_completed and COL_TAMAMLANDI in editor_df.columns:
    _comp_prev = editor_df.loc[editor_df[COL_TAMAMLANDI].map(_coerce_bool_loose)]
    if not _comp_prev.empty:
        with st.expander(
            f"Tamamlanan satırlar — soluk/gri önizleme ({len(_comp_prev)} adet, salt okunur)",
            expanded=False,
        ):
            _show_g = _comp_prev.drop(columns=[COL_AUDIT], errors="ignore")
            st.dataframe(
                _show_g.style.set_properties(
                    **{
                        "background-color": "#e5e7eb",
                        "color": "#4b5563",
                    }
                ),
                use_container_width=True,
                height=min(400, 48 + 32 * min(len(_show_g), 14)),
            )
            st.caption("Düzenleme üstteki ana tablodan yapılır.")
_edited_aligned = _edited_raw.reindex(columns=list(df_display.columns))
edited_df = normalize_dataframe_for_streamlit_editor(_edited_aligned)
_base = df_display.reset_index(drop=True)
_edited_norm = edited_df.reset_index(drop=True)
try:
    _tablo_degisti = not _edited_norm.equals(_base)
except (TypeError, ValueError):
    _tablo_degisti = True
if _tablo_degisti:
    if persist_table_edits(edited_df, toast_message="Tablo güncellendi."):
        st.rerun()

_err = st.session_state.get("_autosave_err")
if _err:
    st.error(_err)