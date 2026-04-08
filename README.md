# 🌪️ spiral - a weird word obfuscation algorithm

```bash
$ python3 spiral.py Top304kMostUsedPasswords.txt
🌪️ spiral.py - a weird word obfuscation algorithm

👀 Reading Top304kMostUsedPasswords.txt...
✅ Read Top304kMostUsedPasswords.txt with 303,872 lines!
✍️ Writing Top304kMostUsedPasswords.txt-spiral.txt...
🎉 Written Top304kMostUsedPasswords-spiral.txt!

👋 Goodbye
```

## ❓ Why?
Word obfuscation could lead us to cracking weird passwords. `spiral.py` was a pattern I was obsessively doing in my head, so I decided to implement it to make it easier for myself.

## ⁉️ How?
`spiral.py` is an alternating pattern:
1. Omit the first character
2. Append character to the right
3. Prepend the next character to the left
4. Append the next character to the right
5. etc.

### ℹ️ Example
```
Hello:

H - Omit
He - Append 'E' to the right
Lhe - Prepend 'L' to the left
Lhel - Append 'L' to the right
Olhel - Prepend 'O' to the left
```
Hence its name - Spiral.
