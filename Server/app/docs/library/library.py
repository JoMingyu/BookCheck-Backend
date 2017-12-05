LIBRARY_POST = {
    'tags': ['도서관'],
    'description': '도서관에 가입(사용자 권한)',
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
            'description': '가입할 도서관 ID',
            'in': 'formData',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '가입 성공',
        },
        '204': {
            'description': '존재하지 않는 도서관 ID'
        },
        '208': {
            'description': '이미 가입되어 있음'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

LIBRARY_GET = {
    'tags': ['도서관'],
    'description': '도서관 리스트 조회(사용자 권한), response의 belonging은 자신이 속해 있는지 여부를 뜻함',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token(JWT ***)',
            'in': 'header',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '리스트 조회 성공',
            'examples': {
                'application/json': [
                    {
                        'id': '1eq65w82e41a6f548461ga6g8r4e',
                        'title': '줜나 사랑스러운 도서관',
                        'belonging': True
                    },
                    {
                        'id': '1d5t8r4e541a6f15e446ga81e52d',
                        'title': '마음으로 읽는 도서관',
                        'belonging': False
                    }
                ]
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

LIBRARY_DELETE = {
    'tags': ['도서관'],
    'description': '도서관에서 탈퇴(사용자 권한)',
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
            'description': '탈퇴할 도서관 ID',
            'in': 'formData',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '탈퇴 성공'
        },
        '204': {
            'description': '존재하지 않는 도서관 ID'
        },
        '208': {
            'description': '애초에 가입되어 있지 않음'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
