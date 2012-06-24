%define	_rc	pre4
Summary:	A command line CD/DVD-Recorder
Summary(es):	Un programa de grabaci�n de CD/DVD
Summary(pl):	Program do nagrywania p�yt CD/DVD
Summary(pt_BR):	Um programa de grava��o de CD/DVD
Summary(ru):	��������� ��� ������ CD/DVD, ����������� �� ��������� ������
Summary(uk):	�������� ��� ������ CD/DVD, ��� ������������ � �������ϧ ��Ҧ���
Name:		cdrkit
Version:	1.0
Release:	0.1
License:	GPL v2
Group:		Applications/System
Source0:	http://debburn.alioth.debian.org/%{name}-%{version}%{_rc}.tar.gz
# Source0-md5:	f475a791cd1d6c82da2dea014a01c9d0
BuildRequires:	cmake
BuildRequires:	libcap-devel
BuildRequires:	libmagic-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cdrkit allows you to create CD's on a CD-Recorder (SCSI/ATAPI).
Supports data, audio, mixed, multi-session and CD+ discs etc.

%description -l pl
Cdrkit pozwala tworzy� CD na nagrywarce CD (SCSI/ATAPI). Obs�uguje
dyski z danymi, d�wi�kiem, mieszane, wielosesyjne, CD+ i inne.

%description -l pt_BR
Cdrkit permite que voc� crie CDs em seu gravador de CDs SCSI/ATAPI. �
poss�vel gravar dados, �udio, misturados, multi-se��o e CD+.

%description -l ru
Cdrkit - ��� ��������� ��� �������� ����� � �������� CD. Cdrecord
�������� �� ������� ������ CD-���������� ������ ��������������,
��������� ������������ multi-session � �������� �� ������� � �������,
��������� ��� ������ ���������.

%description -l uk
Cdrkit - �� �������� ��� ��������� ��Ħ� �� ���������� CD. Cdrecord
������ � �������� ������ CD-�������Ҧ� Ҧ���� �������˦�, ���Φ���
Ц�����դ multi-session � ��צ����Ѥ ��� ������� � �����Ԧ, ����������
��� ������� �������.

%package devel
Summary:	The libschily SCSI user level transport library
Summary(es):	La biblioteca SCSI libschily
Summary(pl):	Biblioteka dost�pu do poziomu SCSI przez u�ytkownika
Summary(pt_BR):	A biblioteca SCSI libschily
Summary(ru):	SCSI-���������� libschily
Summary(uk):	SCSI-¦�̦����� libschily
Group:		Development/Libraries
Obsoletes:	cdrecord-devel

%description devel
The %{name} distribution contains a SCSI user level transport library.
The SCSI library is suitable to talk to any SCSI device without having
a special driver for it. Cdrecord may be easily ported to any system
that has a SCSI device driver similar to the scg driver.

%description devel -l pl
Dystrybucja %{name} zawiera bibliotek� dost�pu do warstwy transportu w
SCSI. Poprzez bibliotek� mo�na komunikowa� si� z dowolnym urz�dzeniem
SCSI bez potrzeby posiadania specjalnego sterownika do tego
urz�dzenia.

%description devel -l pt_BR
O cdrkit cont�m uma biblioteca de transporte de dados por SCSI "user
level". A biblioteca SCSI pode ser usada para conversar com qualquer
dispositivo SCSI sem a necessidade de um driver especial.

%description devel -l ru
����� cdrkit-devel �������� ������������ ���������� �����������������
������ ��� SCSI, ������� ����� �������� � ����� SCSI-����������� ���
������������ �������� ��� ����� ����������. Cdrecord ����� ���� �����
���������� �� ����� ������� � ��������� SCSI-����������, ������� ��
������� scg.

%description devel -l uk
����� cdrkit-devel ͦ����� ���������Φ ¦�̦����� ���������������
Ҧ��� ��� SCSI, �˦ ������ ��������� � ����-���� SCSI-������Ϥ� ���
���æ������� �������� ��� ����� ��������. Cdrecord ���� ���� �����
���������� �� ����-��� ������� � ��������� SCSI-��������, ������ ��
������� scg.

%package cdda2wav
Summary:	Get WAV files from digital audio cd's
Summary(es):	Crea archivos tipo WAV a partir de CDs de audio
Summary(fr):	convertisseur CD-Audio->.WAV
Summary(pl):	Uzyskaj pliki WAV z cyfrowego kompaktu audio
Summary(pt_BR):	Cria arquivos tipo WAV a partir de CDs de �udio
Summary(ru):	������� ��� ��������� ������ .WAV � digital audio CD
Summary(uk):	���̦�� ��� ������æ� ���̦� .WAV � digital audio CD
Group:		Applications/Sound
Provides:	cdda2wav
Obsoletes:	cdda2wav
Obsoletes:	cdrecord-cdda2wav

%description cdda2wav
A sampling utility for cdrom drives that are capable of sending audio
cd data in digital form to your host. Data can be dumped into WAV or
sun format sound files. Options control the recording format
(stereo/mono; 8,12,16 bits; different rates).

%description cdda2wav -l es
Un utilitario para leer m�sicas en accionadores de cdrom capaces de
transmitir datos de CDs de audio en forma digital para tu m�quina. Los
datos pueden ser grabados en formato WAV o sun. Existen opciones para
controlar el formato de la grabaci�n (stereo/mono, 8, 12, 16 bits,
tasas diferentes).

%description cdda2wav -l pl
Narz�dzie do zczytywania danych z nap�d�w cdrom, kt�re s� w stanie
wysy�a� strumie� audio. Dane mog� zosta� zapisane w formacie plik�w
WAV lub suna.

%description cdda2wav -l pt_BR
Um utilit�rio para ler m�sicas em acionadores de cdrom capazes de
transmitir dados de CDs de �udio em forma digital para sua m�quina. Os
dados podem ser gravados em formato WAV ou sun. Existem op��es para
controlar o formato da grava��o (est�reo/mono, 8, 12, 16 bits, taxas
diferentes).

%description cdda2wav -l ru
Cdda2wav - ��� �������, ��������� ��������� ����������� � CD �
�������� ����� � ��������� �� �� ���� � ���� �������� ������ �������
.WAV ��� .sun. ������� ������ �������� ������/����, 8/12/16 ��� �
��������� ������� �������������. Cdda2wav ����� ����� ���� �����������
��� CD-������.

%description cdda2wav -l uk
Cdda2wav - �� �������, ������� ��������� ��Ħ���Φ � CD � �����צ�
���ͦ �� ���Ҧ���� �� �� ���� � �����Ħ �������� ���̦� ������� .WAV
��� .sun. ������� ������ ��������� ������/����, 8/12/16 ¦� �� Ҧ�Φ
������� ����������æ�. Cdda2wav ����� ���� ���� ������������ ��
CD-���ʤ�.

%package readcd
Summary:	Read/Write data Compact Discs
Summary(pl):	Odczytuje/Zapisuje dane z P�yt Kompaktowych
Group:		Applications/System
Obsoletes:	cdrecord-readcd

%description readcd
Read/Write data Compact Discs.

%description readcd -l pl
Odczytuje/Zapisuje dane z P�yt Kompaktowych.

%package utils
Summary:	Dumping and verifying iso9660 images
Summary(pl):	Zrzucanie i weryfikacja obraz�w iso9660
Group:		Applications/System

%description utils
Utility programs for dumping and verifying iso9660 images.

%description utils -l pl
Narz�dzia do zrzucania i weryfikacji obraz�w iso9660.

%package mkisofs
Summary:	Creates an ISO9660 filesystem image
Summary(de):	Erstellt ein Dateisystem-Abbild nach ISO9660
Summary(es):	Crea una imagen de un sistema de archivos ISO9660
Summary(fr):	Cr�e un image syst�me de fichiers ISO9660
Summary(pl):	Tworzy obraz systemu plik�w ISO9660
Summary(pt_BR):	Cria uma imagem de um sistema de arquivos ISO9660
Summary(ru):	������� ����� �������� ������� ISO9660
Summary(tr):	ISO9660 dosya sistemi kopyas� olu�turur
Summary(uk):	������� ����� ������ϧ ������� ISO9660
Group:		Applications/System
Provides:	mkisofs = %{epoch}:%{version}-%{release}
Obsoletes:	mkisofs

%description mkisofs
This is the mkisofs package. It is used to create ISO 9660 file system
images for creating CD-ROMs.

%description mkisofs -l es
Este es el paquete mkisofs. Se le usa para crear im�genes de sistema
de archivos ISO 9660 en la creaci�n de CD-ROMs. Ahora incluye soporte
para hacer CD-ROMs de boot "El Torito".

%description mkisofs -l pl
To jest pakiet mkisofs. Jest on u�ywany do tworzenia obraz�w system�w
plik�w ISO9660 potrzebnych do tworzenia p�yt CD-ROM.

%description mkisofs -l pt_BR
Este � o pacote mkisofs. Ele � usado para criar imagens de sistema de
arquivos ISO 9660 para cria��o de CD-ROMs. Agora inclui suporte para
fazer CD-ROMs de boot "El Torito".

%description mkisofs -l ru
��������� mkisofs ������������ ��� ���������� ������-�����, �.�. ���
���������� �������� ������� ISO9660. Mkisofs ������ ������ ���������
������ ��������� � ���������� �������� ����� ����� ������, �������
������������� �������� ������� ISO9660, ������������ �� �������
����������. Mkisofs ������������ ��� ������ CD-ROM'�� � ��������
��������� �������� ����������� El Torito CD-ROM'��.

%description mkisofs -l uk
�������� mkisofs ����������դ���� ��� Ц�������� ������-�����, ����
�����դ ������� ������� ISO9660. Mkisofs ������ �Φ��� �������� ������
������Ǧ� �� �����դ ¦������ ����� ����� ������, ���� צ���צ���
�����צ� �����ͦ ISO9660, ��������Φ� �� ������� �����Ҧ�. Mkisofs
����������դ���� ��� ������ CD-ROM'�� � ��� Ц������� ���������
�������������� El Torito CD-ROM'��.

%prep
%setup -q -n %{name}-%{version}%{_rc}
sed -i -e 's#/etc/default/wodim#%{_sysconfdir}/wodim.conf#g' cdrecord/defaults.c

%build
%{__make} \
	CC="%{__cc}" \
	COPTOPT="%{rpmcflags}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_libdir},%{_includedir}/schily/scg}

%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

ln -s wodim $RPM_BUILD_ROOT%{_bindir}/cdrecord

install build/*/*.a $RPM_BUILD_ROOT%{_libdir}
install include/*.h $RPM_BUILD_ROOT%{_includedir}/schily
install include/scg/*.h $RPM_BUILD_ROOT%{_includedir}/schily/scg

install cdrecord/wodim.dfl $RPM_BUILD_ROOT/etc/wodim.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/ANNOUNCEMENTs/AN-* Changelog doc/READMEs/{README,README.ATAPI,README.DiskT@2}
%doc doc/READMEs/README.{WORM,audio,cdplus,cdtext,cdrw,clone,copy,mkisofs,multi}
%doc doc/READMEs/README.{raw,rscsi,sony,verify}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/wodim.conf
%attr(755,root,root) %{_bindir}/wodim
%attr(755,root,root) %{_bindir}/cdrecord
%attr(755,root,root) %{_sbindir}/rscsi
%{_mandir}/man1/wodim.1*

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_includedir}/schily

%files cdda2wav
%defattr(644,root,root,755)
%doc doc/cdda2wav/*
%attr(755,root,root) %{_bindir}/cdda2wav
%attr(755,root,root) %{_bindir}/cdda2mp3
%attr(755,root,root) %{_bindir}/cdda2ogg
%{_mandir}/man1/cdda2wav.1*
%{_mandir}/man1/cdda2ogg.1*

%files readcd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/readcd
%{_mandir}/man1/readcd.1*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/devdump
%attr(755,root,root) %{_bindir}/isodebug
%attr(755,root,root) %{_bindir}/isoinfo
%attr(755,root,root) %{_bindir}/isovfy
%attr(755,root,root) %{_bindir}/isodump
%{_mandir}/man8/isodebug.8*
%{_mandir}/man8/isoinfo.8*
%{_mandir}/man8/devdump.8*
%{_mandir}/man8/isovfy.8*
%{_mandir}/man8/isodump.8*

%files mkisofs
%defattr(644,root,root,755)
%doc doc/mkisofs/*
%attr(755,root,root) %{_bindir}/mkisofs
%{_mandir}/man8/mkisofs.8*
