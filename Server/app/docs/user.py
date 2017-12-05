SIGNUP_POST = {
    'tags': ['계정'],
    'description': '일반 사용자 회원가입',
    'parameters': [
        {
            'name': 'id',
            'description': '사용자 ID',
            'in': 'formData',
            'type': 'str',
            'required': True
        },
        {
            'name': 'pw',
            'description': '사용자 비밀번호',
            'in': 'formData',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '회원가입 성공'
        },
        '204': {
            'description': '회원가입 실패(이미 가입된 ID)'
        }
    }
}

AUTH_COMMON_USER_POST = {
    'tags': ['계정'],
    'description': '일반 사용자 로그인. Access Token과 Refresh Token을 반환합니다.',
    'parameters': [
        {
            'name': 'id',
            'description': '사용자 ID',
            'in': 'formData',
            'type': 'str',
            'required': True
        },
        {
            'name': 'pw',
            'description': '사용자 비밀번호',
            'in': 'formData',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '로그인 성공',
            'examples': {
                'application/json': {
                    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MTI2NDAzOTgsImlhdCI6MTUxMjM4MTE5OCwibmJmIjoxNTEyMzgxMTk4LCJqdGkiOiJiNGY5YzIxMS00Mzc4LTRhYmQtOTNlNi00ZjNmYTM1MGZiYWIiLCJpZGVudGl0eSI6ImNpdHk3MzEwQG5hdmVyLmNvbSIsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.ryXc6WsRutdBsZFFDZUtP9Cd_JV8w2fdsI4NE_XICYs",
                    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NDM5MTcxOTgsImlhdCI6MTUxMjM4MTE5OCwibmJmIjoxNTEyMzgxMTk4LCJqdGkiOiJiZDU0Nzk3Zi02MDU0LTQxZjQtOTc5ZC1mYzQ0ZjNjMTM5YzgiLCJpZGVudGl0eSI6IjcwMmRiNmI2LWE5NTEtNDJjZi1hOGRmLTc4MjdiYTRhNzhjYyIsInR5cGUiOiJyZWZyZXNoIn0.CyRz9KMKgWh0Fv1M7DVHTbntBG3uAPKre3fbFUk18eI"
                }
            }
        },
        '401': {
            'description': '로그인 실패(올바르지 않은 ID 또는 PW)'
        }
    }
}

AUTH_ADMIN_POST = {
    'tags': ['계정'],
    'description': '관리자 로그인. Access Token과 Refresh Token을 반환합니다.',
    'parameters': [
        {
            'name': 'id',
            'description': '사용자 ID',
            'in': 'formData',
            'type': 'str',
            'required': True
        },
        {
            'name': 'pw',
            'description': '사용자 비밀번호',
            'in': 'formData',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '로그인 성공',
            'examples': {
                'application/json': {
                    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MTI2NDAzOTgsImlhdCI6MTUxMjM4MTE5OCwibmJmIjoxNTEyMzgxMTk4LCJqdGkiOiJiNGY5YzIxMS00Mzc4LTRhYmQtOTNlNi00ZjNmYTM1MGZiYWIiLCJpZGVudGl0eSI6ImNpdHk3MzEwQG5hdmVyLmNvbSIsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.ryXc6WsRutdBsZFFDZUtP9Cd_JV8w2fdsI4NE_XICYs",
                    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NDM5MTcxOTgsImlhdCI6MTUxMjM4MTE5OCwibmJmIjoxNTEyMzgxMTk4LCJqdGkiOiJiZDU0Nzk3Zi02MDU0LTQxZjQtOTc5ZC1mYzQ0ZjNjMTM5YzgiLCJpZGVudGl0eSI6IjcwMmRiNmI2LWE5NTEtNDJjZi1hOGRmLTc4MjdiYTRhNzhjYyIsInR5cGUiOiJyZWZyZXNoIn0.CyRz9KMKgWh0Fv1M7DVHTbntBG3uAPKre3fbFUk18eI"
                }
            }
        },
        '401': {
            'description': '로그인 실패(올바르지 않은 ID 또는 PW)'
        }
    }
}

REFRESH_POST = {
    'tags': ['계정'],
    'description': '새로운 Access Token 발급',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Refresh Token(JWT ***)',
            'in': 'header',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '인증 성공, 새로운 Access Token 발급',
            'examples': {
                'application/json': {
                    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MTI2NDAzOTgsImlhdCI6MTUxMjM4MTE5OCwibmJmIjoxNTEyMzgxMTk4LCJqdGkiOiJiNGY5YzIxMS00Mzc4LTRhYmQtOTNlNi00ZjNmYTM1MGZiYWIiLCJpZGVudGl0eSI6ImNpdHk3MzEwQG5hdmVyLmNvbSIsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.ryXc6WsRutdBsZFFDZUtP9Cd_JV8w2fdsI4NE_XICYs",
                }
            }
        },
        '205': {
            'description': '다른 디바이스에서 비밀번호가 변경되어 재로그인 필요'
        },
        '403': {
            'description': 'Refresh Token의 내부가 변조되어 재로그인 필요'
        }
    }
}
