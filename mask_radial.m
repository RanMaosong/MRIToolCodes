
%  �ó������ɸ���Ҷ�任������߲���ģʽ�����������
%  ����ˣ�ɳ�� ��۴�ѧ
%  ���ʱ�䣺2011��5��21��
%  �����ʼ�: wsha@eee.hku.hk
%  ת��ʱ�뱣�������ע��

clc;close all;clear all;

N1=320;   %  ģ���С
N2=320;
M=64;    %  ����������   ԭ��ע������Ƕ��� 10%
T=linspace(0,pi,M);     %  �����Ƕ�
Umask=zeros(N2,N1); %  ��ģ����0��1�ֲ���

%  �Ƕ�ѭ��
for i=1:M;  
    kk=tan(T(i));    %  б��
    c1=sqrt(kk^2+1); %  �������ڼ���㵽ֱ�߾���
    %  ����ѭ��
    for m=-N2/2+0.5:N2/2-0.5;
        for n=-N1/2+0.5:N1/2-0.5
            mm=m+N2/2+0.5;
            nn=n+N1/2+0.5;
            d=abs(kk*m-n)/c1;          %  ���빫ʽ
            if (d<1/2)
                Umask(mm,nn)=1;  %  ��ģ����1
            end
        end
    end
end

%  ����ռͼ��ߴ����
disp('������������������')
disp(sum(sum(Umask))/(N1*N2))
%  ����ģʽ
imshow(255*uint8(Umask))
%  ����
% save mask_radial mask_matrix
save radial_320_320_10,