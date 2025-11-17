import sys
from pathlib import Path
try:
    from PyPDF2 import PdfReader
except Exception as e:
    print('MISSING_LIB')
    raise

pdf_path = Path('pdf') / 'UBIQUITY 14.1 Release_v1.pdf'
out_path = Path('tools') / 'UBIQUITY_14_1_text.txt'

if not pdf_path.exists():
    print('PDF_NOT_FOUND:', pdf_path)
    sys.exit(2)

reader = PdfReader(str(pdf_path))
texts = []
for p in reader.pages:
    try:
        texts.append(p.extract_text() or '')
    except Exception:
        texts.append('')

out_path.write_text('\n\n'.join(texts), encoding='utf-8')
print('OK', out_path)
