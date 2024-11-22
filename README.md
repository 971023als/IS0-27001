# ISO/IEC 27001 학습 자료 및 도구

이 저장소는 **ISO/IEC 27001** 인증 준비를 위한 학습 자료, 체크리스트, 문서 템플릿, 그리고 자동화 도구를 제공합니다. 정보보호 관리체계를 효과적으로 설계하고 유지할 수 있도록 필요한 모든 자료와 도구를 포함하고 있습니다.

## 목차
- [개요](#개요)
- [주요 기능](#주요-기능)
- [시스템 요구사항](#시스템-요구사항)
- [설치 방법](#설치-방법)
- [사용법](#사용법)
- [디렉토리 구조](#디렉토리-구조)
- [기여 방법](#기여-방법)
- [라이선스](#라이선스)

## 개요

ISO/IEC 27001은 정보보호 관리체계의 국제 표준으로, 조직이 정보보호 리스크를 체계적으로 관리할 수 있도록 가이드라인을 제공합니다. 이 저장소는 다음과 같은 내용을 포함합니다:
- ISO 27001 인증 기준(Annex A Controls 포함)
- 정보보호 정책, 절차, 가이드라인 문서 템플릿
- 인증 준비 점검표 및 리스크 평가 도구
- 자동화된 보고서 생성 스크립트

## 주요 기능
- **학습 자료**: ISO/IEC 27001 요구사항 및 Annex A 통제 항목 정리
- **체크리스트**: 인증 준비 상태를 점검하기 위한 체크리스트
- **문서 템플릿**: 정보보호 정책, 절차, 리스크 관리 문서 제공
- **리스크 평가 도구**: 리스크 식별 및 분석 자동화
- **보고서 생성**: 결과 보고서를 Word, Excel 형식으로 출력

## 시스템 요구사항
- Python 3.8 이상
- Microsoft Word 또는 Google Docs (문서 템플릿 활용 시)
- Excel 또는 Google Sheets (점검표 활용 시)
- Docker (옵션: 클라우드 배포 환경 테스트 시)

## 설치 방법

1. **저장소 클론**
   ```bash
   git clone https://github.com/username/iso27001-tools.git
   cd iso27001-tools
