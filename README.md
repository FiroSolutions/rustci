# rustci
Continuous integration for Rust

testy with checklibs.py 
```shell
$ python3.7 checklibs.py 
Checking Cargo.toml
Uploading Cargo.toml
Result:
Library: ar Your Version: 0.6.0 Latest Version 0.8.0
 Found a vulnerability for smallvec 
{'smallvec': {'author': 'Rust Project Developers', 'cve': 'RUSTSEC-2019-0012', 'description': 'Description Attempting to call grow on a spilled SmallVec with a value less than the current capacity causes corruption of memory allocator data structures. An attacker that controls the value passed to grow may exploit this flaw to obtain memory contents or gain remote code execution. Credits to @ehuss for discovering, reporting and fixing the bug. More Info https://github.com/servo/rust-smallvec/issues/149 Patched Versions &gt;= 0.6.10', 'link': 'https://rustsec.org/advisories/RUSTSEC-2019-0012.html', 'published_date': '2019-07-19T01:00:00', 'recommendation': 'Update to the latest Rust library version', 'title': 'RUSTSEC-2019-0012: smallvec: Memory corruption in SmallVec::grow()', 'version': 'not set'}}
Library: chttp Your Version: 0 Latest Version 0.5.5
Library: renderdoc Your Version: 1.2 Latest Version 0.7.1
 Found a vulnerability for blake2 
{'blake2': {'author': 'Rust Project Developers', 'cve': 'RUSTSEC-2019-0019', 'description': 'Description When used in conjunction with the Hash-based Message Authentication Code (HMAC), the BLAKE2b and BLAKE2s implementations in blake2 crate versions prior to v0.8.1 used an incorrect block size (32-bytes instead of 64-bytes for BLAKE2s, and 64-bytes instead of 128-bytes for BLAKE2b), causing them to miscompute the MacResult. The v0.8.1 release of the blake2 crate uses the correct block sizes. Note that this advisory only impacts usage of BLAKE2 with HMAC, and does not impact Digest functionality. More Info https://github.com/RustCrypto/MACs/issues/19 Patched Versions &gt;= 0.8.1', 'link': 'https://rustsec.org/advisories/RUSTSEC-2019-0019.html', 'published_date': '2019-08-25T01:00:00', 'recommendation': 'Update to the latest Rust library version', 'title': 'RUSTSEC-2019-0019: blake2: HMAC-BLAKE2 algorithms compute incorrect results', 'version': 'not set'}}
Library: clogger Your Version: 0.1 Latest Version 0.1.0
Library: failure Your Version: 0.1 Latest Version 0.1.7
Library: indicatif Your Version: 0.9 Latest Version 0.14.0
Library: lazy_static Your Version: 1.0.0 Latest Version 1.4.0
Library: log Your Version: 0.4 Latest Version 0.4.10
Library: regex Your Version: 1.0 Latest Version 1.3.7
Library: structopt Your Version: 0.2 Latest Version 0.3.14
Library: tar Your Version: 0.4.20 Latest Version 0.4.26
Library: xdg Your Version: 2.1 Latest Version 2.2.0
Library: xz2 Your Version: 0.1.4 Latest Version 0.1.6
 Found a vulnerability for protobuf 
{'protobuf': {'author': 'Rust Project Developers', 'cve': 'RUSTSEC-2019-0003', 'description': 'Description Affected versions of this crate called Vec::reserve() on user-supplied input. This allows an attacker to cause an Out of Memory condition while calling the vulnerable method on untrusted data. More Info https://github.com/stepancheg/rust-protobuf/issues/411 Patched Versions ^1.7.5 &gt;= 2.6.0', 'link': 'https://rustsec.org/advisories/RUSTSEC-2019-0003.html', 'published_date': '2019-06-08T01:00:00', 'recommendation': 'Update to the latest Rust library version', 'title': 'RUSTSEC-2019-0003: protobuf: Out of Memory in stream::read_raw_bytes_into()', 'version': 'not set'}}
View result on:
https://rust.firosolutions.com/paste/NhVCYTVPTWCMbvHDzSv675FcvH8N5xYbWn8T8gy3bE/jsonresponse

```


## Use:   

# Rust.firosolutions.com

### Shell:  
```shell
$ echo "view it in json"
$ curl -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"urllink":"https://raw.githubusercontent.com/FiroSolutions/vuln_rust/master/Cargo.toml"}' https://rust.firosolutions.com/apiadd
{"pasteid":"IRChsTAM4tWtAg3525VFUyrSSdTtsi73umr2oL4bs4"}

$ curl "https://rust.firosolutions.com/paste/IRChsTAM4tWtAg3525VFUyrSSdTtsi73umr2oL4bs4/jsonresponse"| python -m json.tool
```

In shell you could also upload the Cargo.toml directly to as pasteservice([termbin.com](https://termbin.com) is nice)   
```shell  
$ export tmpcargo="$(cat Cargo.toml | nc termbin.com 9999)"
$ echo $tmpcargo
https://termbin.com/94zm

```

### in Python:     
```python
>>> import requests, json
>>> aa = requests.get('https://rust.firosolutions.com/apiadd', json={'urllink':'https://raw.githubusercontent.com/FiroSolutions/vuln_rust/master/Cargo.toml'}) 
>>> aa.text
'{"pasteid":"cVQGCgcBYXoftYSGNWjzd84vAvmVMCkZPbQiGSHGmmg"}\n'
>>> json.loads(aa.text).get('pasteid')
'cVQGCgcBYXoftYSGNWjzd84vAvmVMCkZPbQiGSHGmmg'
>>> bb = requests.get("https://rust.firosolutions.com/paste/{}/jsonresponse".format(json.loads(aa.text).get('pasteid')))

```



# Use our github app

https://blog.firosolutions.com/2019/09/github-rust-firo/
