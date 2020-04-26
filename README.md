# rustci
Continuous integration for Rust

testy with checklibs.py 
```shell
$ python3.7 checklibs.py 
Checking Cargo.toml
Uploading Cargo.toml
Result:
Library: ar Your Version: 0.6.0 Latest Version 0.8.0
Library: smallvec Your Version: 1.2 Latest Version 1.4.0
Library: chttp Your Version: 0 Latest Version 0.5.5
Library: renderdoc Your Version: 1.2 Latest Version 0.7.1
Library: blake2 Your Version: 1.2 Latest Version 0.8.1
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
Library: protobuf Your Version: 1.2 Latest Version 2.14.0
View result on:
https://rust.firosolutions.com/paste/DklMkRjZ1Jt3PZQdR57QS4sBkK6ZHtzNYqNUyAvG80/jsonresponse

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
