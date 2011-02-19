# -*- coding: cp936 -*-
#whtiefirer
#Python ���ų���
def Partition(ib, fc, Cr):
    wf = fc + 1
    fb = Cr
    sz = ib[fc]
    while 1:
        while ib[wf] < sz and wf < Cr:
            wf = wf + 1
        while ib[fb] > sz:
            fb = fb - 1
        if wf >= fb:
            break
        ib[wf] = ib[wf]^ib[fb]
        ib[fb] = ib[fb]^ib[wf]
        ib[wf] = ib[wf]^ib[fb]
    ib[fc] = ib[fb]
    ib[fb] = sz
    return fb
        
def QuickSort(ib, fc, Cr):
    if fc < Cr:
        fb = Partition(ib, fc, Cr)
        QuickSort(ib, fc, fb - 1)
        QuickSort(ib, fb + 1, Cr)

def BinarySearch(ib, fb, Cr):
    wf = 0
    fc = Cr - 1
    while wf <= fc:
        sz = (wf + fc) / 2
        if fb == ib[sz]:
            return sz;
        if fb > ib[sz]:
            wf = sz + 1
        else: fc = sz - 1
    return -1
        

def main():
    ib = [4, 4, 6, 7, 0, 15, 9, 18, 6, 1]
    fb = [5, 45, 4, 7, 9001, 12, 6, 61, 2, 44, 42]
    print ib
    QuickSort(ib, 0, len(ib) - 1)
    print ib
    print fb
    QuickSort(fb, 0, len(fb) - 1)
    print fb
    wf = int(raw_input("����fb�����䣬�ҽ���ib�б����ҵ�����λ��: "))
    wf = BinarySearch(ib, wf, len(ib) - 1)
    if wf == -1: print '�����fb�������˰ɣ�'
    else: print wf
    wf = int(raw_input("����fb�����䣬�ҽ���fb�б����ҵ�����λ��: "))
    wf = BinarySearch(fb, wf, len(fb) - 1)
    if wf == -1: print 'fbȷʵ����fb�б���...'
    else: print 'fb��ʵ���ǲ���fb�б���...'
    raw_input("Press Enter to continue: ")

main()
