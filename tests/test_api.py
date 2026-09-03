import urllib.request
import urllib.error
import json
import time


BASE_URL = "http://localhost:8000"
API_KEY = "gym-secret-key"


# ============================================================
# TEST GET
# ============================================================

def test_get_endpoint(path):
    try:
        response = urllib.request.urlopen(BASE_URL + path)

        if response.status == 200:
            print(f"PASS: GET {path}")
        else:
            print(f"FAIL: GET {path} -> {response.status}")

    except Exception as error:
        print(f"FAIL: GET {path} -> {error}")


# ============================================================
# TEST SECURITY - POST WITHOUT API KEY
# ============================================================

def test_post_without_api_key():
    data = b'{"name":"Security Test","email":"security-auto@test.de"}'

    request = urllib.request.Request(
        BASE_URL + "/members/",
        data=data,
        headers={
            "Content-Type": "application/json"
        },
        method="POST"
    )

    try:
        urllib.request.urlopen(request)
        print("FAIL: POST without API key was accepted")

    except urllib.error.HTTPError as error:

        if error.code == 401:
            print("PASS: POST without API key -> 401 Unauthorized")
        else:
            print(f"FAIL: Expected 401, received {error.code}")


# ============================================================
# TEST SECURITY - POST WITH CORRECT API KEY
# ============================================================

def test_post_with_api_key():

    # Unique email so the test can be executed several times
    unique_email = f"test-{int(time.time())}@test.de"

    member = {
        "name": "Automatic Test",
        "email": unique_email
    }

    data = json.dumps(member).encode("utf-8")

    request = urllib.request.Request(
        BASE_URL + "/members/",
        data=data,
        headers={
            "Content-Type": "application/json",
            "X-API-Key": API_KEY
        },
        method="POST"
    )

    try:
        response = urllib.request.urlopen(request)

        if response.status == 200:
            print("PASS: POST with correct API key -> 200 OK")
        else:
            print(
                f"FAIL: POST with correct API key -> "
                f"{response.status}"
            )

    except Exception as error:
        print(f"FAIL: POST with correct API key -> {error}")


# ============================================================
# RUN TESTS
# ============================================================

print("=== Gym Management API Tests ===")

test_get_endpoint("/members/")
test_get_endpoint("/courses/")
test_get_endpoint("/registrations/")
test_get_endpoint("/payments/")

test_post_without_api_key()
test_post_with_api_key()
