def bm(pat: str, txt: str) -> int:
  skip = [None] * 256

  for pt1 in range(256):
    skip[pt1] = len(pat)
  for pt in range(len(pat)):
    skip[ord(pat[pt])] = len(pat) - pt - 1
  contador=0
  while pt < len(txt):
    pp = len(pat) - 1
    while txt[pt] == pat[pp]:
      contador +=1
      if pp == 0:
        print("comparisons= ", contador)
        return pt
      pt -= 1
      pp -= 1
    pt += skip[ord(txt[pt])] if skip[ord(txt[pt])] > len(pat) - pp \
      else len(pat) - pp
    contador += 1
  print("comparisons= ", contador)
  return None
#('abcd','acdaabaabaaabb')
#               0123   0123456789012
print('bm=',bm('aa','aaaaaaaaaaaa'))