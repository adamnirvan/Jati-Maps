📍 JatiMaps – Jelajah Kota dengan Cerdas JatiMaps adalah aplikasi visual interaktif berbasis graf yang membantu Anda menemukan rute tercepat antar kota di Indonesia serta menghitung rute optimal keliling semua kota (Traveling Salesman Problem / TSP) menggunakan algoritma Dijkstra dan Brute Force TSP. Dengan dukungan visualisasi graf dinamis, Anda bisa melihat langsung hubungan antar kota dan rute yang dilalui.

🧠 Fitur Utama 🔗 Simulasi Jalur Antar Kota: Tambahkan hingga 10 kota dan 30 jalur acak dengan bobot jarak realistis (10–100 km).

🛰️ Algoritma Dijkstra: Cari jalur tercepat dari satu kota ke kota lain.

🧭 Traveling Salesman (TSP): Hitung rute keliling semua kota dengan jarak minimum menggunakan pendekatan brute force.

🖼️ Visualisasi Interaktif: Lihat graf kota dan rutenya secara langsung dengan bantuan NetworkX dan Matplotlib.

🎯 Nama Kota Nyata: Simulasi menggunakan nama-nama kota besar di Indonesia seperti Surabaya, Jakarta, Yogyakarta, dll.

🚀 Cara Menggunakan Jalankan program Python.

  1. Lihat daftar kota yang tersedia.
  2. Masukkan kota asal dan tujuan (format: Kota_1, Kota_5, dst).

Program akan menampilkan:

  1. Jalur tercepat menggunakan Dijkstra.
  2. Visualisasi graf dan rute.
  3. Rute TSP keliling semua kota dan total jaraknya.

💡 Library yang Digunakan pada JatiMaps

  1. networkx untuk struktur graf dan visualisasi
  2. matplotlib untuk menggambar graf
  3. heapq untuk Dijkstra
  4. itertools.permutations untuk brute-force TSP
  5. random untuk membuat graf acak
