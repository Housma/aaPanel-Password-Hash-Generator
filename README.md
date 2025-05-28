# aaPanel Hash Generator

A simple Python tool to generate aaPanel-style 3-step MD5 password hashes using a given salt.

## Description

This script mimics the exact password hashing mechanism used in aaPanel by performing three steps of MD5 hashing:

1. `MD5(plain_password)`
2. `MD5(step1 + "_bt.cn")`
3. `MD5(step2 + salt)`

Use this to generate valid password hashes for authentication or recovery testing.

> ⚠️ **Important:** Always verify the constant string (`_bt.cn`) used in step 2. It may vary across aaPanel versions. Confirm its presence in `class/public/common.py` on your aaPanel installation.

---

## Tested On

* **aaPanel**: 7.0.20
* **OS**: Ubuntu 20.04.6 LTS (Focal Fossa)

---

## Usage

```bash
python aapanel_hashgen.py -p <password> -s <salt>
```

### Arguments:

* `-p`, `--password` : Plain password string
* `-s`, `--salt`     : Salt string used in hashing

---

## Example

```bash
python aapanel_hashgen.py -p mypassword123 -s abcdefgh
```

### Output:

```
aaPanel Password Hash Generator
-------------------------------
Plain Password : mypassword123
Salt           : abcdefgh
Generated Hash : 8f3e5f0cba3c6b3b1a4cf0584c2f7b9e
```

---

## Author

Huseyin Mardinli
