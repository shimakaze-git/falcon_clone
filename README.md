## falcon Clone

API作成

```
import falcon

app = falcon.API()
print(app)

```

## リクエスト

curl

```
$ curl -v localhost:8000/1/things --header "authorization:custom-token"
```

httpie

```
$ http -v localhost:8000/1/things authorization:custom-token
```

## Python参考資料

- [モジュールのパッケージ化](https://www.python-izm.com/advanced/packaging_module/)
- [__slots__で軽量化](http://coolpythontips.blogspot.jp/2015/12/slots.html)
- [Python高速化テクニック](http://atsuoishimoto.hatenablog.com/entry/20100217/1266418914)

