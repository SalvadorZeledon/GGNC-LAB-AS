PGDMP          
            }            LaBD    17.4    17.4 .               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false                       1262    16387    LaBD    DATABASE     l   CREATE DATABASE "LaBD" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'es-ES';
    DROP DATABASE "LaBD";
                     postgres    false            �            1259    16426 	   contratos    TABLE     &  CREATE TABLE public.contratos (
    id_contratos uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    fechainicio date NOT NULL,
    fechafin date NOT NULL,
    montomensual numeric(10,2),
    estado character varying(50),
    id_estudiantes uuid NOT NULL,
    id_habitaciones uuid NOT NULL
);
    DROP TABLE public.contratos;
       public         heap r       postgres    false            �            1259    16399 	   edificios    TABLE     �   CREATE TABLE public.edificios (
    id_edificios uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    nombre character varying(100) NOT NULL,
    direccion text,
    numerodepisos integer,
    capacidadtotal integer
);
    DROP TABLE public.edificios;
       public         heap r       postgres    false            �            1259    16418    estudiantes    TABLE     �  CREATE TABLE public.estudiantes (
    id_estudiantes uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    nombre character varying(100) NOT NULL,
    apellido character varying(100) NOT NULL,
    carnet character varying(20) NOT NULL,
    fechanacimiento date,
    genero character varying(10),
    carrera character varying(100),
    telefono character varying(20),
    email character varying(100)
);
    DROP TABLE public.estudiantes;
       public         heap r       postgres    false            �            1259    16407    habitaciones    TABLE        CREATE TABLE public.habitaciones (
    id_habitaciones uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    numero character varying(10) NOT NULL,
    piso integer,
    tipo character varying(50),
    capacidad integer,
    estado character varying(50),
    id_edificios uuid NOT NULL
);
     DROP TABLE public.habitaciones;
       public         heap r       postgres    false            �            1259    16453    mantenimiento    TABLE       CREATE TABLE public.mantenimiento (
    id_mantenimiento uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    fechasolicitud date NOT NULL,
    descripcionproblema text,
    fecharesolucion date,
    estado character varying(50),
    id_habitaciones uuid NOT NULL
);
 !   DROP TABLE public.mantenimiento;
       public         heap r       postgres    false            �            1259    16570    notificaciones    TABLE     �  CREATE TABLE public.notificaciones (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    id_estudiante uuid NOT NULL,
    fecha_envio timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    mensaje text,
    estado character varying(20),
    CONSTRAINT notificaciones_estado_check CHECK (((estado)::text = ANY ((ARRAY['Pendiente'::character varying, 'Enviado'::character varying, 'Fallido'::character varying])::text[])))
);
 "   DROP TABLE public.notificaciones;
       public         heap r       postgres    false            �            1259    16442    pagos    TABLE       CREATE TABLE public.pagos (
    id_pagos uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    fechapago date NOT NULL,
    monto numeric(10,2) NOT NULL,
    metodopago character varying(50),
    estadopago character varying(50),
    id_contratos uuid NOT NULL
);
    DROP TABLE public.pagos;
       public         heap r       postgres    false            �            1259    16477    quejas    TABLE     �   CREATE TABLE public.quejas (
    id_quejas uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    fecha date NOT NULL,
    descripcion text,
    estado character varying(50),
    id_estudiantes uuid NOT NULL
);
    DROP TABLE public.quejas;
       public         heap r       postgres    false            �            1259    16490    reportes    TABLE       CREATE TABLE public.reportes (
    id_reportes uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    tiporeporte character varying(100),
    fechageneracion timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    descripcion text,
    rutaarchivo text
);
    DROP TABLE public.reportes;
       public         heap r       postgres    false            �            1259    16563 	   telefonos    TABLE       CREATE TABLE public.telefonos (
    id_telefono uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    nombre character varying(100) NOT NULL,
    numero_telefono character varying(15) NOT NULL,
    fecha_creacion timestamp without time zone DEFAULT now()
);
    DROP TABLE public.telefonos;
       public         heap r       postgres    false            �            1259    16466 
   visitantes    TABLE     .  CREATE TABLE public.visitantes (
    id_visitantes uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    nombre character varying(100) NOT NULL,
    apellido character varying(100),
    dui character varying(20),
    fechavisita timestamp without time zone NOT NULL,
    id_estudiantes uuid NOT NULL
);
    DROP TABLE public.visitantes;
       public         heap r       postgres    false                      0    16426 	   contratos 
   TABLE DATA                 public               postgres    false    221   �:                 0    16399 	   edificios 
   TABLE DATA                 public               postgres    false    218   �=       
          0    16418    estudiantes 
   TABLE DATA                 public               postgres    false    220   �?       	          0    16407    habitaciones 
   TABLE DATA                 public               postgres    false    219   OB                 0    16453    mantenimiento 
   TABLE DATA                 public               postgres    false    223   �D                 0    16570    notificaciones 
   TABLE DATA                 public               postgres    false    228   AG                 0    16442    pagos 
   TABLE DATA                 public               postgres    false    222   ~J                 0    16477    quejas 
   TABLE DATA                 public               postgres    false    225   �L                 0    16490    reportes 
   TABLE DATA                 public               postgres    false    226    O                 0    16563 	   telefonos 
   TABLE DATA                 public               postgres    false    227   &Q                 0    16466 
   visitantes 
   TABLE DATA                 public               postgres    false    224   �Q       `           2606    16431    contratos contratos_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.contratos
    ADD CONSTRAINT contratos_pkey PRIMARY KEY (id_contratos);
 B   ALTER TABLE ONLY public.contratos DROP CONSTRAINT contratos_pkey;
       public                 postgres    false    221            X           2606    16406    edificios edificios_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.edificios
    ADD CONSTRAINT edificios_pkey PRIMARY KEY (id_edificios);
 B   ALTER TABLE ONLY public.edificios DROP CONSTRAINT edificios_pkey;
       public                 postgres    false    218            \           2606    16425 "   estudiantes estudiantes_carnet_key 
   CONSTRAINT     _   ALTER TABLE ONLY public.estudiantes
    ADD CONSTRAINT estudiantes_carnet_key UNIQUE (carnet);
 L   ALTER TABLE ONLY public.estudiantes DROP CONSTRAINT estudiantes_carnet_key;
       public                 postgres    false    220            ^           2606    16423    estudiantes estudiantes_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.estudiantes
    ADD CONSTRAINT estudiantes_pkey PRIMARY KEY (id_estudiantes);
 F   ALTER TABLE ONLY public.estudiantes DROP CONSTRAINT estudiantes_pkey;
       public                 postgres    false    220            Z           2606    16412    habitaciones habitaciones_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.habitaciones
    ADD CONSTRAINT habitaciones_pkey PRIMARY KEY (id_habitaciones);
 H   ALTER TABLE ONLY public.habitaciones DROP CONSTRAINT habitaciones_pkey;
       public                 postgres    false    219            d           2606    16460     mantenimiento mantenimiento_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.mantenimiento
    ADD CONSTRAINT mantenimiento_pkey PRIMARY KEY (id_mantenimiento);
 J   ALTER TABLE ONLY public.mantenimiento DROP CONSTRAINT mantenimiento_pkey;
       public                 postgres    false    223            n           2606    16579 "   notificaciones notificaciones_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.notificaciones
    ADD CONSTRAINT notificaciones_pkey PRIMARY KEY (id);
 L   ALTER TABLE ONLY public.notificaciones DROP CONSTRAINT notificaciones_pkey;
       public                 postgres    false    228            b           2606    16447    pagos pagos_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.pagos
    ADD CONSTRAINT pagos_pkey PRIMARY KEY (id_pagos);
 :   ALTER TABLE ONLY public.pagos DROP CONSTRAINT pagos_pkey;
       public                 postgres    false    222            h           2606    16484    quejas quejas_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.quejas
    ADD CONSTRAINT quejas_pkey PRIMARY KEY (id_quejas);
 <   ALTER TABLE ONLY public.quejas DROP CONSTRAINT quejas_pkey;
       public                 postgres    false    225            j           2606    16498    reportes reportes_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.reportes
    ADD CONSTRAINT reportes_pkey PRIMARY KEY (id_reportes);
 @   ALTER TABLE ONLY public.reportes DROP CONSTRAINT reportes_pkey;
       public                 postgres    false    226            l           2606    16569    telefonos telefonos_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.telefonos
    ADD CONSTRAINT telefonos_pkey PRIMARY KEY (id_telefono);
 B   ALTER TABLE ONLY public.telefonos DROP CONSTRAINT telefonos_pkey;
       public                 postgres    false    227            f           2606    16471    visitantes visitantes_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.visitantes
    ADD CONSTRAINT visitantes_pkey PRIMARY KEY (id_visitantes);
 D   ALTER TABLE ONLY public.visitantes DROP CONSTRAINT visitantes_pkey;
       public                 postgres    false    224            p           2606    16548 '   contratos contratos_id_estudiantes_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.contratos
    ADD CONSTRAINT contratos_id_estudiantes_fkey FOREIGN KEY (id_estudiantes) REFERENCES public.estudiantes(id_estudiantes) ON DELETE CASCADE;
 Q   ALTER TABLE ONLY public.contratos DROP CONSTRAINT contratos_id_estudiantes_fkey;
       public               postgres    false    221    4702    220            q           2606    16523 (   contratos contratos_id_habitaciones_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.contratos
    ADD CONSTRAINT contratos_id_habitaciones_fkey FOREIGN KEY (id_habitaciones) REFERENCES public.habitaciones(id_habitaciones) ON DELETE CASCADE;
 R   ALTER TABLE ONLY public.contratos DROP CONSTRAINT contratos_id_habitaciones_fkey;
       public               postgres    false    219    221    4698            v           2606    16580    notificaciones fk_estudiante    FK CONSTRAINT     �   ALTER TABLE ONLY public.notificaciones
    ADD CONSTRAINT fk_estudiante FOREIGN KEY (id_estudiante) REFERENCES public.estudiantes(id_estudiantes) ON DELETE CASCADE;
 F   ALTER TABLE ONLY public.notificaciones DROP CONSTRAINT fk_estudiante;
       public               postgres    false    220    228    4702            o           2606    16528 +   habitaciones habitaciones_id_edificios_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.habitaciones
    ADD CONSTRAINT habitaciones_id_edificios_fkey FOREIGN KEY (id_edificios) REFERENCES public.edificios(id_edificios) ON DELETE CASCADE;
 U   ALTER TABLE ONLY public.habitaciones DROP CONSTRAINT habitaciones_id_edificios_fkey;
       public               postgres    false    218    219    4696            s           2606    16533 0   mantenimiento mantenimiento_id_habitaciones_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.mantenimiento
    ADD CONSTRAINT mantenimiento_id_habitaciones_fkey FOREIGN KEY (id_habitaciones) REFERENCES public.habitaciones(id_habitaciones) ON DELETE CASCADE;
 Z   ALTER TABLE ONLY public.mantenimiento DROP CONSTRAINT mantenimiento_id_habitaciones_fkey;
       public               postgres    false    223    4698    219            r           2606    16513    pagos pagos_id_contratos_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.pagos
    ADD CONSTRAINT pagos_id_contratos_fkey FOREIGN KEY (id_contratos) REFERENCES public.contratos(id_contratos) ON DELETE CASCADE;
 G   ALTER TABLE ONLY public.pagos DROP CONSTRAINT pagos_id_contratos_fkey;
       public               postgres    false    221    4704    222            u           2606    16553 !   quejas quejas_id_estudiantes_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.quejas
    ADD CONSTRAINT quejas_id_estudiantes_fkey FOREIGN KEY (id_estudiantes) REFERENCES public.estudiantes(id_estudiantes) ON DELETE CASCADE;
 K   ALTER TABLE ONLY public.quejas DROP CONSTRAINT quejas_id_estudiantes_fkey;
       public               postgres    false    225    220    4702            t           2606    16558 )   visitantes visitantes_id_estudiantes_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.visitantes
    ADD CONSTRAINT visitantes_id_estudiantes_fkey FOREIGN KEY (id_estudiantes) REFERENCES public.estudiantes(id_estudiantes) ON DELETE CASCADE;
 S   ALTER TABLE ONLY public.visitantes DROP CONSTRAINT visitantes_id_estudiantes_fkey;
       public               postgres    false    4702    220    224               �  x�ŕOk�G���{s
��H����)�%�&�]�?`0vh���wm��ö�e�����y����7��?ܼ}����'���[���>�|��o�^]OE�	(e�� �r�EYzm��<\S�I��yU e�+d�r�ݟ���;{	�r�ޡ���Hi�K��:���U�=5o�k��CLdD$�����n.�A����8�pG]c�XDe*kK��!	�p$�XQӭ�������n�<��J�W�b8q�@6k&�TK���E�f- �lq�JnPr�T����r�F<K� ���������9�ռ�WL��|<����lL/x����5 �h���ɅAG��L�uU������^�;C�tvlnY���9�g
(�'�?5��{���2L'���yP7�<�Go���5�$�ë��A1mą�F�3�h��Q���v����#Kc�b65�AL!'AWT���>��PN,5d�Gі��l$Uu��i��(��u��*��O�I-G�`UM
��xoC	/��Ţ��
��2�%nC�:0�6��:�9���?Dۥ����`8.��s�<�1
&Ը���~�)�+|�'��1
h+�&uY+"TB^�DFkc:�a"�n��4�gʢґ�g��b���V��<U�'�t6}�^�sk��h�V�G6;�|D�P�na��!�cⷦ�,��HK9����B;���ߡ���         �  x���KkA��~�������O1��"	�ă�~,�$�緕�8�	ӷ~���W������֜�n�͏_�<�7�M:����|��rw�1���ųr߂ :U(-1��j�R�ֶ?�������;���s7�`�?�gsw?��O���8屍C����I��:G��;�ٻ
�+F�i,/�f�_ăq�o&�R��܁I����!D�6(�Z݂p9�
�&�fA	�Kajv�c��cKE��Xp!x?p=�d3A��q��OY�(�,TV��V����8���U�P��@����![T�̕H�`���L��ȇ�f�t*� �Ч �S�X}K1G����,�/�no�0����"�s��J�(Q���LH�����V�U�����!�%�|�j{v9�P��L�������~|I�"`q#�U�^�wiA��߿d_(ÿ����iz      
   �  x����j1�{�·��1�h�E/4��&�:��7��m�u���N=��b�7f?��� �W���vq���v3[\�|���yU�y���S���������r9{s�-Ym� ���H0
KR��F����_oּ����6�Vu�<mDy�
A �������U�l�E�+7u�>�	��-t��ג�M}���:�4�i�����D�ƳsF�
��B�^�
2x/�cC=�� x�����S^��?9>�m��7#�8��re�`OdK���''���54�Π��ԋb\�TǺWB�j���,��U�0�f��\�'Ŝ�!b����:� 4'��!4�"y���CTR��CK\�&��C��;����䵞�c���)p���q@1p�����j�#�a:��sQ�y.�W3v�)�1���%#�%�5AȎr�J
��a��9l�Um<Nuر�NrP�>r�G�����%㬕�!�z����9\�q�rc���S.
���H����`J-J���A����;��QF�4��~�#e�e!X�� ���VP1٨]Nh����uhR{��y۔u~����9f����ϖ��.��nDc��BaI��%�2�yKe<�c/!�Xґ۫-��>������W9=�m��� �ޗ����PTj䞾�����ù��5���?�&xB      	   0  x���MkA�������̗fF�TH�6�&�]�h�Bj���W�>���0�b�^��������js}w�zx��E?�dY�X���W?>�~u�z��9Ѩ��� *S�bTe�f�V��ſ6۱�^�3�{ y�+o�l��Zl���ߝS8vH�'�2H� Z'������.6�B�>��Š�D����Lc���=k|�F�x��k���9f�Kr��ty����^:Ҽ��\v�E�m�4�#W���0E��fiغ��#�)Q��й�w9���07�I�����_Z�=zFp����Z%�'͞b?O��MC� M
U��=��5�R�^�#�d�7א,�H��%��H�-�J��t�ē'�͕�MP��g��AO=�;�c'DE:@�ה�/�(�I��#��uߤTj]&�4)gZ1��c��ҡx��pDѭ)Rg�G�v!�̓�����Wˆ.dm�Fo�
�E�tjO0BqBf��!�2cU�Ǖ؏�����I��U�$P� �8�j(R��HSJ�g�1[H�07��pj�0
63c9�ћ����4F�         �  x�����7���9�� U��9将���ɽT*��������z��L�=�a.b薾���t�������ݛ��/>���~���ɏ���O�_���������z�)�S`H�ĨC΍��^E��e�	b�H����q���<��\�|��ǽ=,?��G"Bxz��q������a]�Z<3���A�
`*��e�ݏ���m����A���B�(��sL��T	B�����A=����O~8=a�z����R.:��4���ݵ]�1��.�B�y�4���йj�6�����1�	�?�uo��#��a�&�#�������H3Wq�f��*�ԡʠ�����yF�g�[8�̱���#Ko�W@csH��5V	��X�R�2V��<|󀄐z�Pc)�;�6�x�#�.}�؏�����5X������2_)�)��P�eHԜ"Xͤ�W���M |	��m?x̸V���>S�����c4Sk�5^�A���1�� HIi�G��	e���[0��r^�o1�����lP��X�O�٦��4��Og�i��-�l��W���i�)� �n��аv(���5�]�au��Y�"s��MAs�k�L�@�	�`��_j���<�9��Sh-Mib0j�s��4j8�c^��n�,G|�cc�on���0>         -  x��ˊ%E����k��K��8-6H+���]dF�3��݋ٻA�Dp��G��G0j�e6Z��*�"+3�����㏺������ty����]�ٍ�y��ݠ���r��y������.��j. M�����1 �B����Ա��k���b	�]QЎe�j�E���B�������s�~�������^�>O��@��Lr���ͷr~���O�X��~�����)ͼ�>��lyn�?>L��0˭�尾�_����A��{���n����c�3�%���S���2�|��7��v�K���������wbZV���ÏO.�=\�#D��Rt��kv�$�@)���w%�����XX�e��Y�8opW�-茪���E�m��S�c��n7��j�)�G���e�(ղ�]	W���8��Q GVKh� ��Z�!��Z��V��,-�a*1@R,bd��஄���_����@�d�#�����Vk.�02�Y1۵У�Q��}�da5�$��4g�p�&&���a���q����N�CeX��:�
R
�.���w����ܭ�U�vniЪ'��%��i����\W0U+�Z)7���2 SL>��%��J�H=Q���-���*a����q�+�!͍Z1֒�V��̥��6�k�Vj���@��s[h�dK��R��^����zr�%,��Z�ܛCͿy��7�����n��Eӷr#lSށR�'��_SΞ/S��%��?��\�a�j��|%@V��l�n�߇pnf�TB-b��0S��5��Yp#�ᓓ? �1�         H  x����N1��<��h�z�8N���8 U�ڻ��h�
�>=[ԥ�Z�h4�$���o������rszv�is��ێ�V�n�7_?|�rr�ysl3t&�H y�0�-�!V��m�1��� d�b��&�=1�7��r%s��M2۬ X�l�̉�S��g������ӿҩ�B�
TB�64#�:Qx�K����x��ݹ>���#`�X����u�A�9ab�F�C9����s��!q4��'K��~_#�����V�<"�H�@38S]�.*�C�z R�hI!&�|ÌP�! �3��)�=`��+`�K�������]��'�Ir@����ˌi�r?pzvi��j+�`u@�y�PD0�*O0���JKy^�(�H��^ �(�R��;�R�R��~6�aУ$��w��S��+v�f� ݲ����K"߽���{�;�[��2���[�NI-{���P	p`���h{}�J��`x�>�gFL���*��:�i��j�b�>�F�]F^Jy����Q
�O�逻1Ș%R��gz
֡����)��N&P����2��T�Ҝm����*{��9:�	6ͨt         :  x����n1��}��-H%����ġ�J�@[�;N"������bx*��ݕ��MF������_�^\-g�Wo�����^~{��n���͇���٦�X�u�y e� ��*-��Z��y�l0`���q=�_�,�?|߿,a}u1��ͽ���d�u�62���5ŀm����ٿ��$�ZH� M�@769���7AȀ��w�8i�Jt4jXAM2$�*3�BG�i��Y�YB�Nԕ��Q�������.�T���-����A	�c�bD����2�%_�P�S��br��	iꖯB�|�x7n�����!�I��������濒�G�ε7_nPv�г��QΤqv�[��@ i�`����҄�v�ӀfB�Nl�LT)�l+���!�Z�29a� "���d�|���ux�����Q�l���]�#_�#b�{��(�d�A�9�$!���l�!����b#N&��Pl8y�fI�J��`k�#�}>~B�jʩ6�^����n���]�I���n���._7�V f���\�>�P�r�E��|''� ���(         �  x����jA��>��V��U����z�0 Q��U��d�d���|�y1{�Aga�afh��T����/O/������.���}�m��z;|}������b��j�ڀlH��u.26�Z5�W�����A�f{So�w��0q@|�p��/7���u���ps�����Â�O���ox�+m����l��i��
&vo6�4�f2��+<�����пR" �-�i)-�ʭp �+�-Rkl�d
�j���߷�J���LC�"h�!�b��s� $Ȅ`���(�@?	7�k��v��$u 0f��E�Yq�4j�/�`�l)OKy��Smel)�9 ׇ�F�V��%�G*�����u�^��+�zWL����7W�~+��YT�'�w�����^��+.;	
�>��)2A��z�3&l���cay64LC���F/����m�	����bND��W���2-�E�d�M}�C��#�bGb]�R,=�I'�V?�0���	�Z��b
[         �   x���=N1��~O�n�`�{��T)"�
�P��k["Z��M�V���A(�S~o���v��e/���Y�>��>,/y̥N�,^7O�m/�ZU(�@�)G���B�BI��2R� �>��!�Y��~�:]۽Fe:v��[�Ԁ��T+iW�-�;�u�X7�M��mQ���8�d�(Ɇ"J��l�|S��x����A�4"� j��L0           x����j1��y���-TŲeKjWYd()4i���BhI���L�E`6g��7G�|yu}���pyu��p���N������~{���O_/�o��rU��Y"�T*Ș��H������ٰ���qww��o���DN�ǷC$(�>���Z�����)w�4������o?�]�w�95�-V�\@&7HBXs��S^�q��ߤ��"�O���2q.V�r�@5t/(F�-0!Fi_�M��D����sc�K)�Ԍ�"-�q���@�p'X^�;E�2�F��XQ�1EĘk�i�ޓ��%�@|�ہp�&lMg)��Pld�r��	C�p3��	������Ca��(��w^�����c�����"Uk��U�A$3#������y E�y�a��+L��(�V�-�e��嬤��� �����S�e����K�x��-ܼp�I(k��;�z�X��ڹl�����j�u��G�-��-��H%&�LOܛ*k���%f/�o/Y���$��6�7_ҁ     