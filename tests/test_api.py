import urllib.request
import urllib.error
import json
import time


BASE_URL = "http://localhost:8000"
API_KEY = "gym-secret-key"


def request_json(path, method="GET", data=None, api_key=None):
    headers = {
        "Content-Type": "application/json"
    }

    if api_key is not None:
        headers["X-API-Key"] = api_key

    body = None

    if data is not None:
        body = json.dumps(data).encode("utf-8")

    request = urllib.request.Request(
        BASE_URL + path,
        data=body,
        headers=headers,
        method=method
    )

    try:
        with urllib.request.urlopen(request) as response:
            response_body = response.read().decode("utf-8")

            if response_body:
                return response.status, json.loads(response_body)

            return response.status, None

    except urllib.error.HTTPError as error:
        error_body = error.read().decode("utf-8")

        try:
            parsed_error = json.loads(error_body)
        except Exception:
            parsed_error = error_body

        return error.code, parsed_error


def print_result(condition, success_message, fail_message):
    if condition:
        print(f"PASS: {success_message}")
    else:
        print(f"FAIL: {fail_message}")


print("=== Gym Management API Tests ===")


# ============================================================
# 1. TEST GET ENDPOINTS
# ============================================================

for path in [
    "/members/",
    "/courses/",
    "/registrations/",
    "/payments/"
]:
    status, _ = request_json(path)

    print_result(
        status == 200,
        f"GET {path} -> 200 OK",
        f"GET {path} -> expected 200, received {status}"
    )


# ============================================================
# 2. TEST POST WITHOUT API KEY
# ============================================================

status, _ = request_json(
    "/members/",
    method="POST",
    data={
        "name": "Security Test",
        "email": "security-no-key@test.de"
    }
)

print_result(
    status == 401,
    "POST without API key -> 401 Unauthorized",
    f"POST without API key -> expected 401, received {status}"
)


# ============================================================
# 3. TEST POST WITH WRONG API KEY
# ============================================================

status, _ = request_json(
    "/members/",
    method="POST",
    api_key="wrong-key",
    data={
        "name": "Wrong Key Test",
        "email": "wrong-key@test.de"
    }
)

print_result(
    status == 401,
    "POST with wrong API key -> 401 Unauthorized",
    f"POST with wrong API key -> expected 401, received {status}"
)


# ============================================================
# 4. CREATE TEMPORARY MEMBER
# ============================================================

unique_email = f"automatic-{int(time.time())}@test.de"

status, created_member = request_json(
    "/members/",
    method="POST",
    api_key=API_KEY,
    data={
        "name": "Automatic Test",
        "email": unique_email
    }
)

print_result(
    status == 200,
    "POST with correct API key -> 200 OK",
    f"POST with correct API key -> expected 200, received {status}"
)

if status != 200 or created_member is None:
    print("STOP: Cannot continue CRUD test because member creation failed.")
    raise SystemExit(1)

member_id = created_member["id"]


# ============================================================
# 5. READ CREATED MEMBER
# ============================================================

status, member = request_json(
    f"/members/{member_id}"
)

print_result(
    status == 200
    and member["name"] == "Automatic Test"
    and member["email"] == unique_email,
    f"GET /members/{member_id} -> created member found",
    f"GET /members/{member_id} -> member not found or wrong data"
)


# ============================================================
# 6. UPDATE MEMBER
# ============================================================

updated_email = f"updated-{int(time.time())}@test.de"

status, updated_member = request_json(
    f"/members/{member_id}",
    method="PUT",
    api_key=API_KEY,
    data={
        "name": "Automatic Test Updated",
        "email": updated_email
    }
)

print_result(
    status == 200
    and updated_member["name"] == "Automatic Test Updated"
    and updated_member["email"] == updated_email,
    f"PUT /members/{member_id} -> member updated",
    f"PUT /members/{member_id} -> update failed"
)


# ============================================================
# 7. DELETE MEMBER
# ============================================================

status, _ = request_json(
    f"/members/{member_id}",
    method="DELETE",
    api_key=API_KEY
)

print_result(
    status == 200,
    f"DELETE /members/{member_id} -> member deleted",
    f"DELETE /members/{member_id} -> expected 200, received {status}"
)


# ============================================================
# 8. CHECK MEMBER IS REALLY DELETED
# ============================================================

status, _ = request_json(
    f"/members/{member_id}"
)

print_result(
    status == 404,
    f"GET /members/{member_id} after delete -> 404 Not Found",
    f"GET /members/{member_id} after delete -> expected 404, received {status}"
)


print("=== Tests completed ===")
