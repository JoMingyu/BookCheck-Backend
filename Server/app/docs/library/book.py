BOOK_POST = {
    'tags': ['책'],
    'description': '도서관에 책 추가(관리자 권한)',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token(JWT ***)',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'library_id',
            'description': '도서관 ID',
            'in': 'formData',
            'type': 'str',
            'required': True
        },
        {
            'name': 'rfid',
            'description': '책의 RFID',
            'in': 'formData',
            'type': 'str',
            'required': True
        },
        {
            'name': 'area',
            'description': '책이 소속된 위치',
            'in': 'formData',
            'type': 'int',
            'required': True
        },
        {
            'name': 'title',
            'description': '책 제목',
            'in': 'formData',
            'type': 'str',
            'required': True
        },
        {
            'name': 'author',
            'description': '책 저자',
            'in': 'formData',
            'type': 'str',
            'required': True
        },
        {
            'name': 'publication_date',
            'description': '출간일(YYYY-MM-DD)',
            'in': 'formData',
            'type': 'str',
            'required': True
        },
        {
            'name': 'summary',
            'description': '책의 요약',
            'in': 'formData',
            'type': 'str',
            'required': True
        },
        {
            'name': 'detail',
            'description': '책 세부 소개',
            'in': 'formData',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '책 등록 성공'
        },
        '204': {
            'description': '존재하지 않는 도서관 ID'
        },
        '208': {
            'description': '이미 등록된 RFID'
        },
        '403': {
            'description': '권한 없음/자기 관할의 도서관이 아님'
        }
    }
}

BOOK_GET = {
    'tags': ['책'],
    'description': '도서관의 책 목록 조회(사용자 권한)',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token(JWT ***)',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'library_id',
            'description': '도서관 ID',
            'in': 'query',
            'type': 'str',
            'required': True
        },
        {
            'name': 'keyword',
            'description': '책 검색 키워드',
            'in': 'query',
            'type': 'str',
            'required': False
        }
    ],
    'responses': {
        '200': {
            'description': '책 목록 조회 성공',
            'examples': {
                'application/json': [
                    {
                        'rfid': 'a1a1a1a1a1a1',
                        'area': 1,
                        'title': '파이썬을 여행하는 히치하이커를 위한 안내서',
                        'author': '케네스 레이즈',
                        'publication_date': '2017-10-31',
                        'summary': '거대한 파이썬 세상을 모험하는 프로그래머를 위한 안내서',
                        'detail': '파이썬을 ‘파이썬답게’ 쓰려면 어떻게 해야 할까? 파이썬스러운 코드라는 게 도대체 어떤 의미일까? 내가 작성한 코드를 파이썬답다고 판단할 수 있는 기준은 무엇일까? 『파이썬을 여행하는 히치하이커를 위한 안내서』는 속 시원하게 답을 찾기 어려운 ‘파이썬다운 프로그램 작성법’을 명료하고 간결하게 정리한 가이드다. 여기에는 초보자는 물론 더 나은 코딩 기술을 고민하는 중급 이상의 파이썬 프로그래머에게 통찰을 주는 내용을 담았다. ',
                        'borrowable': True
                    },
                    {
                        'rfid': 'b1b1b1b1b1b1',
                        'area': 2,
                        'title': '고성능 파이썬',
                        'author': '미샤 고렐릭',
                        'publication_date': '2016-08-10',
                        'summary': '파이썬의 생산성에 컴파일 언어의 성능을 더하다',
                        'detail': '파이썬은 느리다? 이 책은 파이썬의 단 하나의 약점, 성능 문제를 해결해주는 다양한 전략을 소개한다. 파이썬의 관점에서 바라보는 컴퓨터 아키텍처와 동작 원리를 기본으로 깔고, 각종 라이브러리의 올바른 활용법, 행렬과 벡터 연산 가속, 메모리를 효율적으로 쓰는 법, 병목을 찾는 습관과 도구, 네이티브 코드로 컴파일하기 등을 배우고, 파이썬을 성공적으로 도입한 업계 선배들의 경험담과 전략을 듣게 될 것이다. 특히 한국어판에서는 저자의 동의를 얻어 파이썬 2로 작성된 원서의 예제 코드를 파이썬 3에서 실행할 수 있도록 수정하였다.',
                        'borrowable': False
                    }
                ]
            }
        },
        '204': {
            'description': '존재하지 않는 도서관 ID'
        },
        '403': {
            'description': '권한 없음/가입되지 않은 도서관'
        }
    }
}

