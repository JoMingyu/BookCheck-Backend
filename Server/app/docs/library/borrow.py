BORROW_POST = {
    'tags': ['대출'],
    'description': '책 반납(관리자 권한)',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token(JWT ***)',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'rfid',
            'description': '책 RFID',
            'in': 'formData',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '책 반납 성공',
        },
        '204': {
            'description': '존재하지 않는 RFID'
        },
        '208': {
            'description': '반납 불가능한 책(이미 반납되어 대출 가능한 상태)'
        },
        '403': {
            'description': '권한 없음/자기 관할의 도서관이 아님'
        }
    }
}

BORROW_GET = {
    'tags': ['대출'],
    'description': '책 대출(사용자 권한)',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token(JWT ***)',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'rfid',
            'description': '책 RFID',
            'in': 'query',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '책 대출 성공'
        },
        '204': {
            'description': '존재하지 않는 RFID'
        },
        '208': {
            'description': '대출 불가능한 책(이미 대출됨)'
        },
        '403': {
            'description': '권한 없음/가입되지 않은 도서관'
        }
    }
}
