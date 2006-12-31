Summary:	A command line CD/DVD-Recorder
Summary(es):	Un programa de grabaciСn de CD/DVD
Summary(pl):	Program do nagrywania pЁyt CD/DVD
Summary(pt_BR):	Um programa de gravaГЦo de CD/DVD
Summary(ru):	Программа для записи CD/DVD, запускаемая из командной строки
Summary(uk):	Програма для запису CD/DVD, яка запуска╓ться з командно╖ стр╕чки
Name:		cdrkit
Version:	1.1.1
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://debburn.alioth.debian.org/%{name}-%{version}.tar.gz
# Source0-md5:	937f87c13ce268522c14daa9ba8fdbf0
URL:		http://cdrkit.org/
BuildRequires:	cmake
BuildRequires:	libcap-devel
BuildRequires:	libmagic-devel
Provides:	cdrecord
Obsoletes:	cdrecord
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cdrkit allows you to create CD's on a CD-Recorder (SCSI/ATAPI).
Supports data, audio, mixed, multi-session and CD+ discs etc.

%description -l pl
Cdrkit pozwala tworzyФ CD na nagrywarce CD (SCSI/ATAPI). ObsЁuguje
dyski z danymi, d╪wiЙkiem, mieszane, wielosesyjne, CD+ i inne.

%description -l pt_BR
Cdrkit permite que vocЙ crie CDs em seu gravador de CDs SCSI/ATAPI. и
possМvel gravar dados, Аudio, misturados, multi-seГЦo e CD+.

%description -l ru
Cdrkit - это программа для создания аудио и цифровых CD. Cdrecord
работает со многими типами CD-рекордеров разных производителей,
полностью поддерживает multi-session и сообщает об ошибках в формате,
пригодном для чтения человеком.

%description -l uk
Cdrkit - це програма для створення ауд╕о та програмних CD. Cdrecord
працю╓ з багатьма типами CD-рекордер╕в р╕зних виробник╕в, повн╕стю
п╕дтриму╓ multi-session ╕ пов╕домля╓ про помилки у формат╕, придатному
для читання людиною.

%package devel
Summary:	The libschily SCSI user level transport library
Summary(es):	La biblioteca SCSI libschily
Summary(pl):	Biblioteka dostЙpu do poziomu SCSI przez u©ytkownika
Summary(pt_BR):	A biblioteca SCSI libschily
Summary(ru):	SCSI-библиотека libschily
Summary(uk):	SCSI-б╕бл╕отека libschily
Group:		Development/Libraries
Obsoletes:	cdrecord-devel

%description devel
The %{name} distribution contains a SCSI user level transport library.
The SCSI library is suitable to talk to any SCSI device without having
a special driver for it. Cdrecord may be easily ported to any system
that has a SCSI device driver similar to the scg driver.

%description devel -l pl
Dystrybucja %{name} zawiera bibliotekЙ dostЙpu do warstwy transportu w
SCSI. Poprzez bibliotekЙ mo©na komunikowaФ siЙ z dowolnym urz╠dzeniem
SCSI bez potrzeby posiadania specjalnego sterownika do tego
urz╠dzenia.

%description devel -l pt_BR
O cdrkit contИm uma biblioteca de transporte de dados por SCSI "user
level". A biblioteca SCSI pode ser usada para conversar com qualquer
dispositivo SCSI sem a necessidade de um driver especial.

%description devel -l ru
Пакет cdrkit-devel содержит транспортные библиотеки пользовательского
уровня для SCSI, которые могут работать с любым SCSI-устройством без
специального драйвера для этого устройства. Cdrecord может быть легко
портирован на любую систему с драйвером SCSI-устройства, похожим на
драйвер scg.

%description devel -l uk
Пакет cdrkit-devel м╕стить транспортн╕ б╕бл╕отеки користувацького
р╕вня для SCSI, як╕ можуть працювати з будь-яким SCSI-пристро╓м без
спец╕ального драйвера для цього пристрою. Cdrecord може бути легко
портований на будь-яку систему з драйвером SCSI-пристроя, схожим на
драйвер scg.

%package cdda2wav
Summary:	Get WAV files from digital audio cd's
Summary(es):	Crea archivos tipo WAV a partir de CDs de audio
Summary(fr):	convertisseur CD-Audio->.WAV
Summary(pl):	Uzyskaj pliki WAV z cyfrowego kompaktu audio
Summary(pt_BR):	Cria arquivos tipo WAV a partir de CDs de Аudio
Summary(ru):	Утилита для получения файлов .WAV с digital audio CD
Summary(uk):	Утил╕та для генерац╕╖ файл╕в .WAV з digital audio CD
Group:		Applications/Sound
Provides:	cdda2wav = %{epoch}:%{version}-%{release}
Provides:	cdrecord-cdda2wav = %{epoch}:%{version}-%{release}
Provides:	cdrtools-cdda2wav = %{epoch}:%{version}-%{release}
Obsoletes:	cdda2wav
Obsoletes:	cdrecord-cdda2wav
Obsoletes:	cdrtools-cdda2wav

%description cdda2wav
A sampling utility for cdrom drives that are capable of sending audio
cd data in digital form to your host. Data can be dumped into WAV or
sun format sound files. Options control the recording format
(stereo/mono; 8,12,16 bits; different rates).

%description cdda2wav -l es
Un utilitario para leer mЗsicas en accionadores de cdrom capaces de
transmitir datos de CDs de audio en forma digital para tu mАquina. Los
datos pueden ser grabados en formato WAV o sun. Existen opciones para
controlar el formato de la grabaciСn (stereo/mono, 8, 12, 16 bits,
tasas diferentes).

%description cdda2wav -l pl
NarzЙdzie do zczytywania danych z napЙdСw cdrom, ktСre s╠ w stanie
wysyЁaФ strumieЯ audio. Dane mog╠ zostaФ zapisane w formacie plikСw
WAV lub suna.

%description cdda2wav -l pt_BR
Um utilitАrio para ler mЗsicas em acionadores de cdrom capazes de
transmitir dados de CDs de Аudio em forma digital para sua mАquina. Os
dados podem ser gravados em formato WAV ou sun. Existem opГУes para
controlar o formato da gravaГЦo (estИreo/mono, 8, 12, 16 bits, taxas
diferentes).

%description cdda2wav -l ru
Cdda2wav - это сэмплер, способный считывать аудиоданные с CD в
цифровой форме и сохранять их на диск в виде звуковых файлов формата
.WAV или .sun. Форматы записи включают стерео/моно, 8/12/16 бит и
различные частоты дискретизации. Cdda2wav также может быть использован
как CD-плейер.

%description cdda2wav -l uk
Cdda2wav - це семплер, здатний зчитувати ауд╕одан╕ ╕ CD у цифров╕й
форм╕ та збер╕гати ╖х на диск у вигляд╕ звукових файл╕в формату .WAV
або .sun. Формати запису включають стерео/моно, 8/12/16 б╕т та р╕зн╕
частоты дискретизац╕╖. Cdda2wav також може бути використаний як
CD-плей╓р.

%package readcd
Summary:	Read/Write data Compact Discs
Summary(pl):	Odczytuje/Zapisuje dane z PЁyt Kompaktowych
Group:		Applications/System
Provides:	cdrecord-readcd = %{epoch}:%{version}-%{release}
Provides:	cdrtools-readcd = %{epoch}:%{version}-%{release}
Obsoletes:	cdrecord-readcd
Obsoletes:	cdrtools-readcd

%description readcd
Read/Write data Compact Discs.

%description readcd -l pl
Odczytuje/Zapisuje dane z PЁyt Kompaktowych.

%package utils
Summary:	Dumping and verifying iso9660 images
Summary(pl):	Zrzucanie i weryfikacja obrazСw iso9660
Group:		Applications/System
Provides:	cdrtools-utils = %{epoch}:%{version}-%{release}
Obsoletes:	cdrtools-utils

%description utils
Utility programs for dumping and verifying iso9660 images.

%description utils -l pl
NarzЙdzia do zrzucania i weryfikacji obrazСw iso9660.

%package mkisofs
Summary:	Creates an ISO9660 filesystem image
Summary(de):	Erstellt ein Dateisystem-Abbild nach ISO9660
Summary(es):	Crea una imagen de un sistema de archivos ISO9660
Summary(fr):	CrИe un image systХme de fichiers ISO9660
Summary(pl):	Tworzy obraz systemu plikСw ISO9660
Summary(pt_BR):	Cria uma imagem de um sistema de arquivos ISO9660
Summary(ru):	Создает образ файловой системы ISO9660
Summary(tr):	ISO9660 dosya sistemi kopyasЩ oluЧturur
Summary(uk):	Створю╓ образ файлово╖ системи ISO9660
Group:		Applications/System
Provides:	cdrtools-mkisofs = %{epoch}:%{version}-%{release}
Provides:	mkisofs = %{epoch}:%{version}-%{release}
Obsoletes:	cdrtools-mkisofs
Obsoletes:	mkisofs

%description mkisofs
This is the mkisofs package. It is used to create ISO 9660 file system
images for creating CD-ROMs.

%description mkisofs -l es
Este es el paquete mkisofs. Se le usa para crear imАgenes de sistema
de archivos ISO 9660 en la creaciСn de CD-ROMs. Ahora incluye soporte
para hacer CD-ROMs de boot "El Torito".

%description mkisofs -l pl
To jest pakiet mkisofs. Jest on u©ywany do tworzenia obrazСw systemСw
plikСw ISO9660 potrzebnych do tworzenia pЁyt CD-ROM.

%description mkisofs -l pt_BR
Este И o pacote mkisofs. Ele И usado para criar imagens de sistema de
arquivos ISO 9660 para criaГЦo de CD-ROMs. Agora inclui suporte para
fazer CD-ROMs de boot "El Torito".

%description mkisofs -l ru
Программа mkisofs используется для подготовки мастер-диска, т.е. она
генерирует файловую систему ISO9660. Mkisofs делает снимок заданного
дерева каталогов и генерирует бинарный образ этого дерева, который
соответствует файловой системе ISO9660, записываемой на блочное
устройство. Mkisofs используется для записи CD-ROM'ов и включает
поддержку создания загружаемых El Torito CD-ROM'ов.

%description mkisofs -l uk
Програма mkisofs використову╓ться для п╕дготовки мастер-диску, вона
генеру╓ файлову систему ISO9660. Mkisofs робить зн╕мок заданого дерева
каталог╕в та генеру╓ б╕нарный образ цього дерева, який в╕дпов╕да╓
файлов╕й систем╕ ISO9660, записуван╕й на блочний пристр╕й. Mkisofs
використову╓ться для запису CD-ROM'╕в ╕ ма╓ п╕дтримку створення
завантажуваних El Torito CD-ROM'╕в.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	COPTOPT="%{rpmcflags}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_libdir},%{_includedir}/cdrkit/usal}

%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

ln -s wodim $RPM_BUILD_ROOT%{_bindir}/cdrecord
ln -s icedax $RPM_BUILD_ROOT%{_bindir}/cdda2wav
ln -s genisoimage $RPM_BUILD_ROOT%{_bindir}/mkisofs
ln -s readom $RPM_BUILD_ROOT%{_bindir}/readcd

install build/*/*.a $RPM_BUILD_ROOT%{_libdir}
install include/*.h $RPM_BUILD_ROOT%{_includedir}/cdrkit
install include/usal/*.h $RPM_BUILD_ROOT%{_includedir}/cdrkit/usal

install wodim/wodim.dfl $RPM_BUILD_ROOT%{_sysconfdir}/wodim.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ABOUT FAQ FORK TODO Changelog
%doc doc/ANNO* doc/README* doc/wodim
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/wodim.conf
%attr(755,root,root) %{_bindir}/wodim
%attr(755,root,root) %{_bindir}/cdrecord
%attr(755,root,root) %{_sbindir}/netscsid
%{_mandir}/man1/wodim.1*

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_includedir}/cdrkit

%files cdda2wav
%defattr(644,root,root,755)
%doc doc/icedax/*
%attr(755,root,root) %{_bindir}/icedax
%attr(755,root,root) %{_bindir}/cdda2mp3
%attr(755,root,root) %{_bindir}/cdda2ogg
%{_mandir}/man1/icedax.1*
%{_mandir}/man1/cdda2ogg.1*

%files readcd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/read*
%{_mandir}/man1/read*.1*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/devdump
%attr(755,root,root) %{_bindir}/isodebug
%attr(755,root,root) %{_bindir}/isoinfo
%attr(755,root,root) %{_bindir}/isovfy
%attr(755,root,root) %{_bindir}/isodump
%{_mandir}/man1/isodebug.1*
%{_mandir}/man1/isoinfo.1*
%{_mandir}/man1/devdump.1*
%{_mandir}/man1/isovfy.1*
%{_mandir}/man1/isodump.1*

%files mkisofs
%defattr(644,root,root,755)
%doc doc/genisoimage/*
%attr(755,root,root) %{_bindir}/mkisofs
%attr(755,root,root) %{_bindir}/genisoimage
%{_mandir}/man1/genisoimage.1*
%{_mandir}/man5/genisoimagerc.5*
