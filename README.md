# rustci
Continuous integration for Rust



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
