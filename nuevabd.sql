PGDMP         .            
    x            Humanamente    12.1    12.1     !           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            "           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            #           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            $           1262    115766    Humanamente    DATABASE     �   CREATE DATABASE "Humanamente" WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'English_United States.1252' LC_CTYPE = 'English_United States.1252';
    DROP DATABASE "Humanamente";
                postgres    false            �            1259    115767    citas    TABLE     �   CREATE TABLE public.citas (
    id integer NOT NULL,
    fecha date NOT NULL,
    hora time without time zone NOT NULL,
    descripcion character varying,
    pacienteid integer NOT NULL,
    doctorid integer
);
    DROP TABLE public.citas;
       public         heap    postgres    false            �            1259    115783    doctores    TABLE     �   CREATE TABLE public.doctores (
    id integer NOT NULL,
    nombre character varying NOT NULL,
    telefono integer,
    especializacion character varying
);
    DROP TABLE public.doctores;
       public         heap    postgres    false            �            1259    115791    medicamentos    TABLE     �   CREATE TABLE public.medicamentos (
    id integer NOT NULL,
    nombre character varying NOT NULL,
    disponible integer NOT NULL,
    precio numeric,
    vencimiento character varying,
    codigo character varying
);
     DROP TABLE public.medicamentos;
       public         heap    postgres    false            �            1259    115775 	   pacientes    TABLE     �   CREATE TABLE public.pacientes (
    id integer NOT NULL,
    nombre character varying NOT NULL,
    cita boolean,
    telefono integer
);
    DROP TABLE public.pacientes;
       public         heap    postgres    false            �            1259    115802    secretarias    TABLE     �   CREATE TABLE public.secretarias (
    id integer NOT NULL,
    nombre character varying NOT NULL,
    username character varying NOT NULL,
    password character varying NOT NULL
);
    DROP TABLE public.secretarias;
       public         heap    postgres    false                      0    115767    citas 
   TABLE DATA           S   COPY public.citas (id, fecha, hora, descripcion, pacienteid, doctorid) FROM stdin;
    public          postgres    false    202   �                 0    115783    doctores 
   TABLE DATA           I   COPY public.doctores (id, nombre, telefono, especializacion) FROM stdin;
    public          postgres    false    204                    0    115791    medicamentos 
   TABLE DATA           [   COPY public.medicamentos (id, nombre, disponible, precio, vencimiento, codigo) FROM stdin;
    public          postgres    false    205   �                 0    115775 	   pacientes 
   TABLE DATA           ?   COPY public.pacientes (id, nombre, cita, telefono) FROM stdin;
    public          postgres    false    203                    0    115802    secretarias 
   TABLE DATA           E   COPY public.secretarias (id, nombre, username, password) FROM stdin;
    public          postgres    false    206   �       �
           2606    115774    citas Citas_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.citas
    ADD CONSTRAINT "Citas_pkey" PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.citas DROP CONSTRAINT "Citas_pkey";
       public            postgres    false    202            �
           2606    115790    doctores doctores_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.doctores
    ADD CONSTRAINT doctores_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.doctores DROP CONSTRAINT doctores_pkey;
       public            postgres    false    204            �
           2606    115798    medicamentos medicamentos_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.medicamentos
    ADD CONSTRAINT medicamentos_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.medicamentos DROP CONSTRAINT medicamentos_pkey;
       public            postgres    false    205            �
           2606    115782    pacientes pacientes_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.pacientes
    ADD CONSTRAINT pacientes_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.pacientes DROP CONSTRAINT pacientes_pkey;
       public            postgres    false    203            �
           2606    115809    secretarias secretarias_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.secretarias
    ADD CONSTRAINT secretarias_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.secretarias DROP CONSTRAINT secretarias_pkey;
       public            postgres    false    206               u   x�E�A
�@D�u�)r�����Ev�7��M t�F��$�|�	S�DMFh۫���w��AP�K����S^��i'�&e2����o��Ƃ��)�cC4��?�<�;.׃�� ]�          c   x�3��*M�SH-J��4426153��(�L���O��2��)�,V��/ �� �s��f�d�+�f��s����[��(,�L,)J����� Z��         }   x�E̻
�@����ìs���R$��4�F������0�����S����r�讞�*��q������a�gx��l�M#��@�"����s�G�(�{3r�׺��f�N�DC �/I"~         k   x��1�0 ��~E^�D �3� ;K��m$D�*���|ҵ�H�B����a�g0�����{!�`؞����Ջ�0����ä�Լ��1��\�"����� �l�         a   x�3��*M��t�LM��442�2��M,�LTp+M�+I-��܀R\Ɯ>���
��y)�U`�!H؄3��X!�b��1�XE� \�`m�ih����� �$     