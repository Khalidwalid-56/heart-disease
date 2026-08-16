<!DOCTYPE html>
<html lang="ar" dir="rtl" class="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>EGO SUPPLEMENT | المكملات الغذائية الرياضية الأفضل في مصر</title>
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <!-- FontAwesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <!-- Google Fonts: Cairo & Montserrat -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700;800;900&family=Montserrat:wght@700;800;900&display=swap" rel="stylesheet">

  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            brand: {
              gold: '#d97706',
              goldHover: '#b45309',
              dark: '#1f2937',
              card: '#ffffff',
              cardBorder: '#e5e7eb',
              accent: '#f59e0b',
              lightBg: '#f9fafb'
            }
          },
          fontFamily: {
            sans: ['Cairo', 'sans-serif'],
            en: ['Montserrat', 'sans-serif']
          }
        }
      }
    }
  </script>
  <style>
    body {
      background-color: #f9fafb;
      color: #1f2937;
      font-family: 'Cairo', sans-serif;
    }
    .font-en {
      font-family: 'Montserrat', sans-serif;
    }
    /* Custom Light Scrollbar */
    ::-webkit-scrollbar {
      width: 8px;
    }
    ::-webkit-scrollbar-track {
      background: #f3f4f6;
    }
    ::-webkit-scrollbar-thumb {
      background: #d1d5db;
      border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #d97706;
    }
  </style>
</head>
<body class="min-h-screen flex flex-col justify-between selection:bg-amber-500 selection:text-white">

  <!-- Application Shell Mount Point -->
  <div id="app" class="flex-grow flex flex-col"></div>

  <!-- WhatsApp Floating Action Button -->
  <a id="whatsapp-btn" href="#" target="_blank" class="fixed bottom-6 right-6 bg-emerald-600 hover:bg-emerald-700 text-white p-4 rounded-full shadow-2xl z-50 flex items-center justify-center transition-transform hover:scale-110">
    <i class="fab fa-whatsapp text-2xl"></i>
  </a>

  <!-- Toast Container -->
  <div id="toast-container" class="fixed top-5 left-5 z-50 space-y-3 pointer-events-none"></div>

  <!-- JS Interactive Core Architecture -->
  <script>
    // Initial Database & State Representation
    const INITIAL_DATA = {
      store: {
        name: "EGO SUPPLEMENT",
        phone: "+201000000000",
        whatsapp: "201000000000",
        email: "support@egosupplement.com",
        freeShippingThreshold: 2000,
        announcement: "⚡ شحن مجاني لكافة المحافظات للطلبات الأعلى من 2000 جنيه!"
      },
      categories: [
        { id: "cat-1", name: "بروتين", slug: "protein", icon: "fa-drumstick-bite" },
        { id: "cat-2", name: "كرياتين", slug: "creatine", icon: "fa-bolt" },
        { id: "cat-3", name: "قبل التمرين (Pre-Workout)", slug: "pre-workout", icon: "fa-fire" },
        { id: "cat-4", name: "أحماض أمينية (BCAA & EAA)", slug: "amino", icon: "fa-capsules" },
        { id: "cat-5", name: "فيتامينات وصحة عامة", slug: "vitamins", icon: "fa-heart-pulse" },
        { id: "cat-6", name: "زيادة الوزن (Mass Gainers)", slug: "mass", icon: "fa-dumbbell" }
      ],
      shippingZones: [
        { id: "zone-1", governorate: "القاهرة", cost: 50 },
        { id: "zone-2", governorate: "الجيزة", cost: 50 },
        { id: "zone-3", governorate: "الإسكندرية", cost: 65 },
        { id: "zone-4", governorate: "الشرقية", cost: 70 },
        { id: "zone-5", governorate: "الدقهلية", cost: 70 },
        { id: "zone-6", governorate: "القليوبية", cost: 60 },
        { id: "zone-7", governorate: "الغربية", cost: 70 },
        { id: "zone-8", governorate: "بورسعيد", cost: 75 },
        { id: "zone-9", governorate: "السويس", cost: 75 }
      ],
      discounts: [
        { code: "EGO10", type: "PERCENTAGE", value: 10, minOrder: 500, active: true },
        { code: "BIG500", type: "FIXED", value: 500, minOrder: 3000, active: true }
      ],
      products: [
        {
          id: "prod-1",
          sku: "EGO-WHEY-01",
          name: "EGO ISO-PURE Whey Protein 2Kg",
          category: "protein",
          brand: "EGO SUPPLEMENT",
          price: 2800,
          oldPrice: 3200,
          stock: 15,
          rating: 4.9,
          reviewsCount: 38,
          badge: "الأكثر مبيعاً",
          isFeatured: true,
          image: "https://images.unsplash.com/photo-1593095948071-474c5cc2989d?w=600&auto=format&fit=crop&q=80",
          flavors: ["شوكولاتة ناعمة", "فانيليا آيس كريم", "كراميل ممتع"],
          sizes: ["2 كجم (66 جرعة)"],
          description: "واي بروتين معزول نقي 100% عالي الجودة سريع الامتصاص، خالي من السكر والمواد المضافة الهادفة لتسريع الاستشفاء البنائي.",
          ingredients: "Whey Protein Isolate, Natural & Artificial Flavors, Sucralose, Digestive Enzymes.",
          nutrition: "27g Protein, 0g Fat, 1g Carb, 110 Calories per scoop."
        },
        {
          id: "prod-2",
          sku: "EGO-CREA-01",
          name: "EGO Micro-Pure Creatine Monohydrate 300g",
          category: "creatine",
          brand: "EGO SUPPLEMENT",
          price: 950,
          oldPrice: 1200,
          stock: 22,
          rating: 4.8,
          reviewsCount: 64,
          badge: "خصم مميز",
          isFeatured: true,
          image: "https://images.unsplash.com/photo-1579722821273-0f6c7d44362f?w=600&auto=format&fit=crop&q=80",
          flavors: ["بدون نكهة", "توت أزرق سينمائي"],
          sizes: ["300 جرام (60 جرعة)"],
          description: "كرياتين ميكرونايزد شديد النقاء بتركيز 200 Mesh لضمان ذوبان فوري وزيادة مستويات القوة والانفجار العضلي.",
          ingredients: "100% Pure Micronized Creatine Monohydrate.",
          nutrition: "5g Creatine Monohydrate per serving."
        },
        {
          id: "prod-3",
          sku: "EGO-PRE-01",
          name: "EGO OVERLOAD Pre-Workout 400g",
          category: "pre-workout",
          brand: "EGO SUPPLEMENT",
          price: 1350,
          oldPrice: 1600,
          stock: 8,
          rating: 5.0,
          reviewsCount: 19,
          badge: "جديد",
          isFeatured: true,
          image: "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=600&auto=format&fit=crop&q=80",
          flavors: ["حامض الليمون والنعناع", "فرولة وفواكه استوائية"],
          sizes: ["400 جرام (30 جرعة)"],
          description: "تركيبة خارقة للضخ العضلي والتركيز الشديد وتحفيز الطاقة دون أثر هبوط، يحتوي على 350mg كافيين و6g سترولين مالات.",
          ingredients: "L-Citrulline Malate, Beta-Alanine, Caffeine Anhydrous, Alpha-GPC.",
          nutrition: "6000mg Citrulline, 3200mg Beta-Alanine, 350mg Caffeine."
        },
        {
          id: "prod-4",
          sku: "EGO-BCAA-01",
          name: "EGO Matrix BCAA + EAA Recovery",
          category: "amino",
          brand: "EGO SUPPLEMENT",
          price: 1100,
          oldPrice: 1300,
          stock: 12,
          rating: 4.7,
          reviewsCount: 15,
          badge: "استشفاء سريع",
          isFeatured: false,
          image: "https://images.unsplash.com/photo-1546483875-ad9014c88eba?w=600&auto=format&fit=crop&q=80",
          flavors: ["بطيخ منعش", "عصير حامض"],
          sizes: ["390 جرام (30 جرعة)"],
          description: "مزيج الأحماض الأمينية الأساسية مع الكلكتروليتات لمنع التفكك العضلي وتوفير التغذية الهيدروليكية الكاملة.",
          ingredients: "L-Leucine, L-Isoleucine, L-Valine, Essential Amino Acids, Electrolyte Blend.",
          nutrition: "7g BCAA, 3g EAA, 500mg Electrolytes."
        },
        {
          id: "prod-5",
          sku: "EGO-VIT-01",
          name: "EGO Multi-Vit Sports Performance",
          category: "vitamins",
          brand: "EGO SUPPLEMENT",
          price: 650,
          oldPrice: 750,
          stock: 30,
          rating: 4.9,
          reviewsCount: 42,
          badge: "صحة عامة",
          isFeatured: false,
          image: "https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?w=600&auto=format&fit=crop&q=80",
          flavors: ["أقراص بلا نكهة"],
          sizes: ["90 قرص (30 يوم)"],
          description: "مجمع فيتامينات ومعادن مخصص للرياضيين لدعم المناعة والأداء البدني والعمليات الحيوية.",
          ingredients: "Vitamin A, C, D3, E, Complex B, Zinc, Magnesium, Ashwagandha Extract.",
          nutrition: "100% Daily Value of Essential Micronutrients."
        },
        {
          id: "prod-6",
          sku: "EGO-MASS-01",
          name: "EGO Titan Mass Gainer 5Kg",
          category: "mass",
          brand: "EGO SUPPLEMENT",
          price: 2400,
          oldPrice: 2750,
          stock: 4,
          rating: 4.6,
          reviewsCount: 28,
          badge: "ضخامة عضلية",
          isFeatured: true,
          image: "https://images.unsplash.com/photo-1579722820308-d74e571900a9?w=600&auto=format&fit=crop&q=80",
          flavors: ["شوكولاتة بالحليب", "موز غني"],
          sizes: ["5 كجم (30 جرعة ضخمة)"],
          description: "مكتسب الكتلة العضلية العملاق المزود بـ 1250 سعرة حرارية و 50 جم بروتين لزيادة الوزن والكتلة العضلية بسرعة.",
          ingredients: "Complex Carbs Blend, Whey Protein Concentrate, Micellar Casein, MCT Oils.",
          nutrition: "1250 Calories, 50g Protein, 250g Carbs per serving."
        }
      ],
      orders: [
        {
          id: "EGO-8921-102",
          customerName: "أحمد محمود",
          customerPhone: "01012345678",
          governorate: "القاهرة",
          city: "مدينة نصر",
          address: "شارع الطيران - العمارة 14 - شقة 3",
          total: 3750,
          paymentMethod: "COD",
          paymentStatus: "تم الدفع",
          orderStatus: "تم التسليم",
          date: "2026-08-10",
          items: [
            { name: "EGO ISO-Pure Whey Protein 2Kg", qty: 1, price: 2800, flavor: "شوكولاتة ناعمة" },
            { name: "EGO Micro-Pure Creatine 300g", qty: 1, price: 950, flavor: "بدون نكهة" }
          ]
        },
        {
          id: "EGO-9210-405",
          customerName: "سارة حسن",
          customerPhone: "01234567890",
          governorate: "الإسكندرية",
          city: "سموحة",
          address: "شارع ألبير الأول - شقة 12",
          total: 1415,
          paymentMethod: "ONLINE_CARD",
          paymentStatus: "معلق الدفع",
          orderStatus: "قيد التحضير",
          date: "2026-08-16",
          items: [
            { name: "EGO OVERLOAD Pre-Workout 400g", qty: 1, price: 1350, flavor: "حامض الليمون" }
          ]
        }
      ]
    };

    // State Management
    class StoreState {
      constructor() {
        this.data = JSON.parse(localStorage.getItem('EGO_APP_DATA_LIGHT')) || INITIAL_DATA;
        this.cart = JSON.parse(localStorage.getItem('EGO_APP_CART_LIGHT')) || [];
        this.currentView = 'home';
        this.selectedProductId = null;
        this.filterCategory = 'all';
        this.searchQuery = '';
        this.sortBy = 'featured';
        this.appliedDiscount = null;
        this.lastCreatedOrder = null;
        this.adminTab = 'dashboard';
        this.adminLoggedIn = false;
      }

      save() {
        localStorage.setItem('EGO_APP_DATA_LIGHT', JSON.stringify(this.data));
        localStorage.setItem('EGO_APP_CART_LIGHT', JSON.stringify(this.cart));
      }

      addToCart(productId, flavor, size, qty = 1) {
        const product = this.data.products.find(p => p.id === productId);
        if (!product) return;

        if (product.stock < qty) {
          showToast(`عذراً، المتوفر حالياً من هذا المنتج هو ${product.stock} فقط`, "error");
          return;
        }

        const existingIndex = this.cart.findIndex(
          item => item.productId === productId && item.flavor === flavor && item.size === size
        );

        if (existingIndex > -1) {
          this.cart[existingIndex].qty += qty;
        } else {
          this.cart.push({
            productId,
            name: product.name,
            price: product.price,
            image: product.image,
            flavor: flavor || (product.flavors[0] || ''),
            size: size || (product.sizes[0] || ''),
            qty
          });
        }

        this.save();
        showToast("تم إضافة المنتج إلى سلة التسوق بنجاح! 🛒", "success");
        renderApp();
      }

      removeFromCart(index) {
        this.cart.splice(index, 1);
        this.save();
        renderApp();
      }

      updateCartQty(index, delta) {
        if (this.cart[index]) {
          this.cart[index].qty += delta;
          if (this.cart[index].qty <= 0) {
            this.cart.splice(index, 1);
          }
        }
        this.save();
        renderApp();
      }

      getCartSubtotal() {
        return this.cart.reduce((sum, item) => sum + (item.price * item.qty), 0);
      }

      getDiscountAmount() {
        if (!this.appliedDiscount) return 0;
        const subtotal = this.getCartSubtotal();
        if (subtotal < this.appliedDiscount.minOrder) return 0;

        if (this.appliedDiscount.type === 'PERCENTAGE') {
          return (subtotal * this.appliedDiscount.value) / 100;
        } else {
          return this.appliedDiscount.value;
        }
      }

      clearCart() {
        this.cart = [];
        this.appliedDiscount = null;
        this.save();
      }
    }

    const state = new StoreState();

    // Helper Toast System
    function showToast(message, type = "info") {
      const toastContainer = document.getElementById('toast-container');
      const toast = document.createElement('div');
      
      const bgColor = type === "success" ? "bg-emerald-600" : type === "error" ? "bg-red-600" : "bg-amber-600";
      toast.className = `${bgColor} text-white px-5 py-3 rounded-xl shadow-xl font-bold text-sm flex items-center gap-3 transition-all duration-300 transform translate-x-12 opacity-0 pointer-events-auto`;
      toast.innerHTML = `<i class="fas ${type === 'success' ? 'fa-check-circle' : 'fa-exclamation-circle'}"></i> <span>${message}</span>`;
      
      toastContainer.appendChild(toast);
      
      setTimeout(() => {
        toast.classList.remove('translate-x-12', 'opacity-0');
      }, 50);

      setTimeout(() => {
        toast.classList.add('opacity-0', 'translate-x-12');
        setTimeout(() => toast.remove(), 300);
      }, 3500);
    }

    // Set WhatsApp Link
    document.getElementById('whatsapp-btn').href = `https://wa.me/${state.data.store.whatsapp}?text=${encodeURIComponent("مرحباً EGO SUPPLEMENT، أريد الاستفسار عن المكملات الغذائية المتاحة.")}`;

    // Application Renderer Component Router
    function renderApp() {
      const app = document.getElementById('app');
      app.innerHTML = '';

      // Header Navigation Bar
      app.appendChild(renderHeader());

      // Main View Router
      const mainContainer = document.createElement('main');
      mainContainer.className = "flex-grow";

      switch (state.currentView) {
        case 'home':
          mainContainer.appendChild(renderHomeView());
          break;
        case 'shop':
          mainContainer.appendChild(renderShopView());
          break;
        case 'product':
          mainContainer.appendChild(renderProductDetailView());
          break;
        case 'cart':
          mainContainer.appendChild(renderCartView());
          break;
        case 'checkout':
          mainContainer.appendChild(renderCheckoutView());
          break;
        case 'order-success':
          mainContainer.appendChild(renderOrderSuccessView());
          break;
        case 'admin':
          mainContainer.appendChild(renderAdminView());
          break;
        default:
          mainContainer.appendChild(renderHomeView());
      }

      app.appendChild(mainContainer);

      // Footer Navigation
      if (state.currentView !== 'admin') {
        app.appendChild(renderFooter());
      }
    }

    // 1. Header Component
    function renderHeader() {
      const header = document.createElement('header');
      header.className = "sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-gray-200 text-gray-900 shadow-sm";

      const cartCount = state.cart.reduce((total, i) => total + i.qty, 0);

      header.innerHTML = `
        <!-- Top Announcement Bar -->
        <div class="bg-amber-500 text-white text-xs font-black py-2 px-4 text-center tracking-wider uppercase shadow-inner">
          ${state.data.store.announcement}
        </div>

        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
          <!-- Logo -->
          <div onclick="navigateTo('home')" class="cursor-pointer flex items-center gap-2.5 group">
            <div class="w-10 h-10 bg-amber-600 text-white font-black text-2xl flex items-center justify-center rounded-lg shadow group-hover:bg-amber-700 transition">
              E
            </div>
            <div class="flex flex-col">
              <span class="font-black text-2xl tracking-wider leading-none font-en text-gray-900">EGO<span class="text-amber-600">.</span></span>
              <span class="text-[9px] tracking-[0.25em] text-gray-500 font-extrabold uppercase leading-none mt-1 font-en">SUPPLEMENT</span>
            </div>
          </div>

          <!-- Navigation Links -->
          <nav class="hidden md:flex items-center gap-8 font-bold text-sm tracking-wide uppercase text-gray-700">
            <button onclick="navigateTo('home')" class="${state.currentView === 'home' ? 'text-amber-600 font-black' : 'hover:text-amber-600'} transition">الرئيسية</button>
            <button onclick="navigateTo('shop', {category: 'all'})" class="${state.currentView === 'shop' && state.filterCategory === 'all' ? 'text-amber-600 font-black' : 'hover:text-amber-600'} transition">الكل</button>
            <button onclick="navigateTo('shop', {category: 'protein'})" class="${state.filterCategory === 'protein' ? 'text-amber-600 font-black' : 'hover:text-amber-600'} transition">بروتين</button>
            <button onclick="navigateTo('shop', {category: 'creatine'})" class="${state.filterCategory === 'creatine' ? 'text-amber-600 font-black' : 'hover:text-amber-600'} transition">كرياتين</button>
            <button onclick="navigateTo('shop', {category: 'pre-workout'})" class="${state.filterCategory === 'pre-workout' ? 'text-amber-600 font-black' : 'hover:text-amber-600'} transition">Pre-Workout</button>
          </nav>

          <!-- Right Action Icons -->
          <div class="flex items-center gap-4">
            <button onclick="navigateTo('shop')" class="text-gray-600 hover:text-gray-900 p-2 transition">
              <i class="fas fa-search text-lg"></i>
            </button>
            
            <button onclick="navigateTo('cart')" class="relative bg-amber-50 border border-amber-200 p-2.5 rounded-xl hover:border-amber-500 transition shadow-sm">
              <i class="fas fa-shopping-cart text-amber-700 text-lg"></i>
              ${cartCount > 0 ? `<span class="absolute -top-2 -right-2 bg-amber-600 text-white text-xs font-black rounded-full h-5 w-5 flex items-center justify-center shadow-md">${cartCount}</span>` : ''}
            </button>

            <button onclick="navigateTo('admin')" class="bg-gray-100 hover:bg-gray-200 text-xs font-bold text-gray-800 px-3.5 py-2.5 rounded-xl border border-gray-300 transition flex items-center gap-2 shadow-sm">
              <i class="fas fa-user-shield text-amber-600"></i>
              <span class="hidden sm:inline">لوحة التحكم</span>
            </button>
          </div>
        </div>
      `;

      return header;
    }

    // 2. Home Page View Component
    function renderHomeView() {
      const div = document.createElement('div');
      
      const featuredProducts = state.data.products.filter(p => p.isFeatured);

      div.innerHTML = `
        <!-- Hero Section -->
        <section class="relative bg-gradient-to-b from-amber-50/50 via-white to-gray-50 text-gray-900 border-b border-gray-200 py-16 lg:py-24 overflow-hidden">
          <div class="absolute inset-0 opacity-10 bg-[radial-gradient(#d97706_1px,transparent_1px)] [background-size:20px_20px]"></div>
          
          <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 flex flex-col lg:flex-row items-center justify-between gap-12">
            <div class="max-w-2xl text-center lg:text-right space-y-6">
              <div class="inline-flex items-center gap-2 bg-amber-100 border border-amber-300 text-amber-800 px-4 py-1.5 rounded-full text-xs font-black tracking-widest uppercase shadow-sm">
                <i class="fas fa-bolt text-amber-600"></i> مكملات نقية وموثوقة 100%
              </div>
              <h1 class="text-4xl sm:text-6xl font-black leading-tight tracking-tight text-gray-900">
                تخطى حدودك مع <br/>
                <span class="text-transparent bg-clip-text bg-gradient-to-r from-amber-600 via-amber-500 to-amber-700 font-en">EGO SUPPLEMENT</span>
              </h1>
              <p class="text-gray-600 text-base sm:text-lg font-medium leading-relaxed">
                تركيبات رياضية فاخرة ومختبرة لضمان أقصى أداء، زيادة الكتلة العضلية، وتسريع الاستشفاء البدني بأعلى معايير الجودة العالمية.
              </p>
              <div class="flex flex-wrap justify-center lg:justify-start gap-4 pt-2">
                <button onclick="navigateTo('shop')" class="bg-amber-600 hover:bg-amber-700 text-white font-black px-8 py-4 rounded-xl text-sm uppercase tracking-wider transition transform hover:-translate-y-0.5 shadow-lg shadow-amber-600/20">
                  تسوق المنتجات الآن <i class="fas fa-arrow-left mr-2"></i>
                </button>
                <button onclick="navigateTo('shop', {category: 'protein'})" class="bg-white hover:bg-gray-50 text-gray-800 font-extrabold border border-gray-300 px-8 py-4 rounded-xl text-sm uppercase transition shadow-sm">
                  استكشف الواي بروتين
                </button>
              </div>
            </div>

            <!-- Hero Feature Card -->
            <div class="relative w-full max-w-md">
              <div class="bg-gradient-to-tr from-amber-400 to-amber-600 rounded-2xl p-1 shadow-2xl">
                <div class="bg-white rounded-xl p-6 text-center space-y-4 shadow-inner">
                  <span class="bg-amber-600 text-white font-black text-xs px-3.5 py-1 rounded-full uppercase shadow">العرض الحصري اليوم</span>
                  <img src="${featuredProducts[0]?.image}" alt="${featuredProducts[0]?.name}" class="w-full h-64 object-cover rounded-xl shadow-sm">
                  <h3 class="font-black text-xl text-gray-900">${featuredProducts[0]?.name}</h3>
                  <div class="text-2xl font-black text-amber-600 font-en">${featuredProducts[0]?.price} EGP</div>
                  <button onclick="navigateTo('product', {id: '${featuredProducts[0]?.id}'})" class="w-full bg-amber-600 hover:bg-amber-700 text-white font-bold py-3.5 rounded-xl transition shadow">
                    عرض التفاصيل الشاملة
                  </button>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- Categories Section -->
        <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
          <div class="flex justify-between items-end mb-10">
            <div>
              <h2 class="text-2xl sm:text-3xl font-black text-gray-900">تسوق حسب الفئة</h2>
              <p class="text-gray-500 text-sm mt-1">اختر المكمل المخصص لأهدافك الرياضية اليوم</p>
            </div>
          </div>

          <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-4">
            ${state.data.categories.map(cat => `
              <div onclick="navigateTo('shop', {category: '${cat.slug}'})" class="bg-white border border-gray-200 hover:border-amber-500 p-6 rounded-2xl text-center cursor-pointer transition transform hover:-translate-y-1 shadow-sm hover:shadow-md group">
                <div class="w-12 h-12 bg-amber-50 text-amber-600 rounded-xl flex items-center justify-center mx-auto mb-3 text-xl group-hover:bg-amber-600 group-hover:text-white transition shadow-sm">
                  <i class="fas ${cat.icon}"></i>
                </div>
                <h3 class="font-bold text-sm text-gray-800 group-hover:text-amber-600">${cat.name}</h3>
              </div>
            `).join('')}
          </div>
        </section>

        <!-- Featured Products -->
        <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 border-t border-gray-200">
          <div class="flex justify-between items-end mb-10">
            <div>
              <h2 class="text-2xl sm:text-3xl font-black text-gray-900">المنتجات المميزة</h2>
              <p class="text-gray-500 text-sm mt-1">المكملات الأعلى طلباً وتقييماً من قبل أبطالنا</p>
            </div>
            <button onclick="navigateTo('shop')" class="text-amber-600 hover:text-amber-700 font-bold text-sm flex items-center gap-1">
              عرض الكتالوج كامل <i class="fas fa-chevron-left text-xs"></i>
            </button>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            ${featuredProducts.map(product => renderProductCardHTML(product)).join('')}
          </div>
        </section>

        <!-- Why Choose Us -->
        <section class="bg-gray-100 border-y border-gray-200 py-16 my-12">
          <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8 text-center">
              <div class="p-6 bg-white rounded-2xl border border-gray-200 shadow-sm space-y-3">
                <div class="w-16 h-16 bg-amber-50 text-amber-600 rounded-2xl flex items-center justify-center mx-auto text-2xl shadow-sm">
                  <i class="fas fa-certificate"></i>
                </div>
                <h3 class="font-bold text-lg text-gray-900">منتجات أصلية 100%</h3>
                <p class="text-gray-500 text-sm leading-relaxed">جميع المكملات مستوردة ومفحوصة معملياً لضمان النقاء الكامل وتاريخ الصلاحية.</p>
              </div>

              <div class="p-6 bg-white rounded-2xl border border-gray-200 shadow-sm space-y-3">
                <div class="w-16 h-16 bg-amber-50 text-amber-600 rounded-2xl flex items-center justify-center mx-auto text-2xl shadow-sm">
                  <i class="fas fa-truck-fast"></i>
                </div>
                <h3 class="font-bold text-lg text-gray-900">توصيل سريع لكل مصر</h3>
                <p class="text-gray-500 text-sm leading-relaxed">شحن أمن وسريع لجميع المحافظات مع إمكانية الدفع عند الاستلام المعاين قبل الدفع.</p>
              </div>

              <div class="p-6 bg-white rounded-2xl border border-gray-200 shadow-sm space-y-3">
                <div class="w-16 h-16 bg-amber-50 text-amber-600 rounded-2xl flex items-center justify-center mx-auto text-2xl shadow-sm">
                  <i class="fas fa-headset"></i>
                </div>
                <h3 class="font-bold text-lg text-gray-900">دعم واستشارات رياضية</h3>
                <p class="text-gray-500 text-sm leading-relaxed">فريق متكامل من المتخصصين لمساعدتك في اختيار الكورس المناسب لأهدافك.</p>
              </div>
            </div>
          </div>
        </section>
      `;

      return div;
    }

    // Product Card Template Generator (Light Mode)
    function renderProductCardHTML(product) {
      return `
        <div class="bg-white border border-gray-200 rounded-2xl overflow-hidden flex flex-col justify-between hover:border-amber-500 transition duration-300 shadow-sm hover:shadow-lg group">
          <div class="relative">
            <!-- Badge -->
            ${product.badge ? `<span class="absolute top-3 right-3 bg-amber-600 text-white font-black text-xs px-2.5 py-1 rounded-lg z-10 uppercase shadow-md">${product.badge}</span>` : ''}
            
            <div class="overflow-hidden h-64 bg-gray-50 cursor-pointer flex items-center justify-center" onclick="navigateTo('product', {id: '${product.id}'})">
              <img src="${product.image}" alt="${product.name}" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
            </div>
          </div>

          <div class="p-5 flex-grow flex flex-col justify-between space-y-4">
            <div>
              <div class="text-xs text-amber-600 font-extrabold uppercase tracking-wider mb-1 font-en">${product.brand}</div>
              <h3 onclick="navigateTo('product', {id: '${product.id}'})" class="font-bold text-base text-gray-900 hover:text-amber-600 cursor-pointer line-clamp-2 transition">${product.name}</h3>
              
              <div class="flex items-center gap-1 text-amber-500 text-xs mt-2">
                <i class="fas fa-star"></i>
                <span class="font-bold text-gray-800">${product.rating}</span>
                <span class="text-gray-400">(${product.reviewsCount} تقييم)</span>
              </div>
            </div>

            <div class="pt-3 border-t border-gray-100 flex items-center justify-between">
              <div>
                <div class="text-xl font-black text-gray-900 font-en">${product.price} <span class="text-xs text-gray-500">EGP</span></div>
                ${product.oldPrice ? `<div class="text-xs text-gray-400 line-through font-en">${product.oldPrice} EGP</div>` : ''}
              </div>

              <button onclick="state.addToCart('${product.id}')" class="bg-amber-600 hover:bg-amber-700 text-white font-extrabold px-4 py-2.5 rounded-xl text-xs transition flex items-center gap-1.5 shadow">
                <i class="fas fa-cart-plus"></i> أضف للسلة
              </button>
            </div>
          </div>
        </div>
      `;
    }

    // 3. Catalog / Shop View
    function renderShopView() {
      const div = document.createElement('div');
      div.className = "max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10";

      // Filtering Logic
      let filtered = state.data.products.filter(p => {
        const matchesCategory = state.filterCategory === 'all' || p.category === state.filterCategory;
        const matchesSearch = p.name.toLowerCase().includes(state.searchQuery.toLowerCase()) || 
                              p.sku.toLowerCase().includes(state.searchQuery.toLowerCase());
        return matchesCategory && matchesSearch;
      });

      // Sorting
      if (state.sortBy === 'price-low') {
        filtered.sort((a, b) => a.price - b.price);
      } else if (state.sortBy === 'price-high') {
        filtered.sort((a, b) => b.price - a.price);
      }

      div.innerHTML = `
        <div class="mb-8 space-y-2">
          <h1 class="text-3xl font-black text-gray-900">متجر EGO SUPPLEMENT</h1>
          <p class="text-gray-500 text-sm">استعرض تشكيلة المكملات الغذائية الاحترافية كاملة</p>
        </div>

        <!-- Controls: Search & Category Filter -->
        <div class="bg-white border border-gray-200 p-4 rounded-2xl mb-8 flex flex-col md:flex-row gap-4 justify-between items-center shadow-sm">
          <!-- Search Box -->
          <div class="relative w-full md:w-80">
            <input 
              type="text" 
              placeholder="ابحث بالاسم أو SKU..." 
              value="${state.searchQuery}"
              oninput="state.searchQuery = this.value; renderApp();"
              class="w-full bg-gray-50 border border-gray-200 text-gray-900 rounded-xl px-4 py-2.5 text-sm pr-10 focus:outline-none focus:border-amber-500"
            >
            <i class="fas fa-search absolute left-3 top-3.5 text-gray-400 text-sm"></i>
          </div>

          <!-- Category Buttons -->
          <div class="flex items-center gap-2 overflow-x-auto w-full md:w-auto pb-2 md:pb-0">
            <button onclick="state.filterCategory = 'all'; renderApp();" class="px-4 py-2 rounded-xl text-xs font-bold whitespace-nowrap ${state.filterCategory === 'all' ? 'bg-amber-600 text-white' : 'bg-gray-100 text-gray-700 hover:bg-gray-200'}">الكل</button>
            ${state.data.categories.map(c => `
              <button onclick="state.filterCategory = '${c.slug}'; renderApp();" class="px-4 py-2 rounded-xl text-xs font-bold whitespace-nowrap ${state.filterCategory === c.slug ? 'bg-amber-600 text-white' : 'bg-gray-100 text-gray-700 hover:bg-gray-200'}">${c.name}</button>
            `).join('')}
          </div>

          <!-- Sort Select -->
          <select onchange="state.sortBy = this.value; renderApp();" class="bg-gray-50 border border-gray-200 text-gray-800 text-xs font-bold rounded-xl px-3.5 py-2.5 focus:outline-none">
            <option value="featured" ${state.sortBy === 'featured' ? 'selected' : ''}>الأبرز</option>
            <option value="price-low" ${state.sortBy === 'price-low' ? 'selected' : ''}>السعر: من الأقل للأعلى</option>
            <option value="price-high" ${state.sortBy === 'price-high' ? 'selected' : ''}>السعر: من الأعلى للأقل</option>
          </select>
        </div>

        <!-- Products Grid -->
        ${filtered.length > 0 ? `
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            ${filtered.map(p => renderProductCardHTML(p)).join('')}
          </div>
        ` : `
          <div class="text-center py-20 bg-white border border-gray-200 rounded-2xl shadow-sm">
            <i class="fas fa-box-open text-4xl text-gray-300 mb-3"></i>
            <h3 class="text-lg font-bold text-gray-800">لم يتم العثور على منتجات</h3>
            <p class="text-gray-500 text-sm mt-1">جرب البحث بكلمات أخرى أو اختر فئة مختلفة.</p>
          </div>
        `}
      `;

      return div;
    }

    // 4. Product Details View
    function renderProductDetailView() {
      const product = state.data.products.find(p => p.id === state.selectedProductId);
      const div = document.createElement('div');
      div.className = "max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10";

      if (!product) {
        div.innerHTML = `<div class="text-center py-20 text-gray-500">المنتج غير موجود.</div>`;
        return div;
      }

      let selectedFlavor = product.flavors[0] || '';
      let selectedSize = product.sizes[0] || '';

      div.innerHTML = `
        <button onclick="navigateTo('shop')" class="text-amber-600 font-bold text-sm mb-6 inline-flex items-center gap-2 hover:underline">
          <i class="fas fa-arrow-right"></i> العودة للكتالوج
        </button>

        <div class="bg-white border border-gray-200 rounded-3xl p-6 lg:p-10 grid grid-cols-1 lg:grid-cols-2 gap-10 shadow-sm">
          <!-- Image Gallery -->
          <div class="space-y-4">
            <div class="bg-gray-50 rounded-2xl overflow-hidden h-96 flex items-center justify-center border border-gray-200 p-4">
              <img src="${product.image}" alt="${product.name}" class="max-h-full object-contain">
            </div>
          </div>

          <!-- Product Specifications -->
          <div class="space-y-6">
            <div>
              <span class="text-xs text-amber-600 font-extrabold uppercase tracking-widest font-en">${product.brand} | SKU: ${product.sku}</span>
              <h1 class="text-2xl sm:text-3xl font-black text-gray-900 mt-1">${product.name}</h1>
              
              <div class="flex items-center gap-3 mt-3">
                <div class="flex items-center text-amber-500 text-sm">
                  <i class="fas fa-star"></i>
                  <span class="font-bold mr-1 text-gray-800">${product.rating}</span>
                </div>
                <span class="text-gray-400 text-sm">(${product.reviewsCount} تقييم معتمد)</span>
                <span class="bg-emerald-50 text-emerald-700 text-xs font-bold px-2.5 py-1 rounded-lg border border-emerald-200">متوفر بالمخزون (${product.stock})</span>
              </div>
            </div>

            <!-- Price -->
            <div class="p-4 bg-gray-50 rounded-2xl border border-gray-200 flex items-center gap-4">
              <div class="text-3xl font-black text-amber-600 font-en">${product.price} <span class="text-sm text-gray-500">EGP</span></div>
              ${product.oldPrice ? `<div class="text-base text-gray-400 line-through font-en">${product.oldPrice} EGP</div>` : ''}
            </div>

            <!-- Flavors Selection -->
            ${product.flavors.length > 0 ? `
              <div>
                <label class="block text-xs font-bold text-gray-700 uppercase mb-2">النكهات المتاحة:</label>
                <div class="flex flex-wrap gap-2" id="flavor-options">
                  ${product.flavors.map((f, idx) => `
                    <button type="button" onclick="selectOption('flavor', '${f}', this)" class="option-btn px-4 py-2 rounded-xl text-xs font-bold border ${idx === 0 ? 'border-amber-600 bg-amber-50 text-amber-700' : 'border-gray-200 bg-gray-50 text-gray-700'}">${f}</button>
                  `).join('')}
                </div>
              </div>
            ` : ''}

            <!-- Size Selection -->
            ${product.sizes.length > 0 ? `
              <div>
                <label class="block text-xs font-bold text-gray-700 uppercase mb-2">الحجم / العبوة:</label>
                <div class="flex flex-wrap gap-2" id="size-options">
                  ${product.sizes.map((s, idx) => `
                    <button type="button" onclick="selectOption('size', '${s}', this)" class="option-btn px-4 py-2 rounded-xl text-xs font-bold border ${idx === 0 ? 'border-amber-600 bg-amber-50 text-amber-700' : 'border-gray-200 bg-gray-50 text-gray-700'}">${s}</button>
                  `).join('')}
                </div>
              </div>
            ` : ''}

            <!-- CTA Actions -->
            <div class="flex items-center gap-4 pt-2">
              <button onclick="state.addToCart('${product.id}', '${selectedFlavor}', '${selectedSize}', 1)" class="flex-1 bg-amber-600 hover:bg-amber-700 text-white font-black py-4 rounded-xl text-base transition flex items-center justify-center gap-2 shadow-lg shadow-amber-600/20">
                <i class="fas fa-shopping-cart"></i> إضافة إلى السلة
              </button>
            </div>

            <!-- Accordion Details -->
            <div class="border-t border-gray-200 pt-6 space-y-4 text-sm text-gray-700">
              <div>
                <h4 class="font-bold text-gray-900 mb-1">وصف المنتج:</h4>
                <p class="leading-relaxed text-gray-600">${product.description}</p>
              </div>

              <div>
                <h4 class="font-bold text-gray-900 mb-1">المكونات:</h4>
                <p class="font-en text-xs text-gray-600">${product.ingredients}</p>
              </div>

              <div>
                <h4 class="font-bold text-gray-900 mb-1">القيمة الغذائية:</h4>
                <p class="font-en text-xs text-gray-600">${product.nutrition}</p>
              </div>
            </div>
          </div>
        </div>
      `;

      return div;
    }

    function selectOption(type, value, btn) {
      const container = btn.parentElement;
      container.querySelectorAll('.option-btn').forEach(b => {
        b.className = 'option-btn px-4 py-2 rounded-xl text-xs font-bold border border-gray-200 bg-gray-50 text-gray-700';
      });
      btn.className = 'option-btn px-4 py-2 rounded-xl text-xs font-bold border border-amber-600 bg-amber-50 text-amber-700';
    }

    // 5. Shopping Cart View
    function renderCartView() {
      const div = document.createElement('div');
      div.className = "max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-10";

      const subtotal = state.getCartSubtotal();
      const discount = state.getDiscountAmount();
      const grandTotal = Math.max(0, subtotal - discount);

      div.innerHTML = `
        <h1 class="text-3xl font-black text-gray-900 mb-8">سلة التسوق</h1>

        ${state.cart.length > 0 ? `
          <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
            <!-- Items List -->
            <div class="lg:col-span-2 space-y-4">
              ${state.cart.map((item, index) => `
                <div class="bg-white border border-gray-200 p-4 rounded-2xl flex items-center gap-4 shadow-sm">
                  <img src="${item.image}" alt="${item.name}" class="w-20 h-20 object-cover rounded-xl bg-gray-50 border border-gray-100">
                  
                  <div class="flex-grow">
                    <h3 class="font-bold text-gray-900 text-sm">${item.name}</h3>
                    <div class="text-xs text-gray-500 mt-1">النكهة: ${item.flavor} | الحجم: ${item.size}</div>
                    <div class="font-bold text-amber-600 font-en mt-1">${item.price} EGP</div>
                  </div>

                  <!-- Qty Controls -->
                  <div class="flex items-center gap-2 bg-gray-50 border border-gray-200 rounded-xl p-1">
                    <button onclick="state.updateCartQty(${index}, -1)" class="w-7 h-7 flex items-center justify-center text-gray-600 hover:text-gray-900 font-bold">-</button>
                    <span class="font-bold text-sm w-6 text-center font-en text-gray-900">${item.qty}</span>
                    <button onclick="state.updateCartQty(${index}, 1)" class="w-7 h-7 flex items-center justify-center text-gray-600 hover:text-gray-900 font-bold">+</button>
                  </div>

                  <!-- Remove -->
                  <button onclick="state.removeFromCart(${index})" class="text-gray-400 hover:text-red-600 p-2 transition">
                    <i class="fas fa-trash-can"></i>
                  </button>
                </div>
              `).join('')}
            </div>

            <!-- Summary Card -->
            <div class="bg-white border border-gray-200 p-6 rounded-2xl space-y-6 h-fit shadow-sm">
              <h2 class="font-bold text-lg text-gray-900 border-b border-gray-100 pb-3">ملخص الطلب</h2>

              <!-- Promo Code Input -->
              <div>
                <label class="block text-xs font-bold text-gray-700 uppercase mb-2">كود الخصم:</label>
                <div class="flex gap-2">
                  <input type="text" id="promo-code-input" placeholder="مثال: EGO10" class="bg-gray-50 border border-gray-200 text-gray-900 rounded-xl px-3 py-2 text-xs uppercase flex-grow focus:outline-none focus:border-amber-500 font-en">
                  <button onclick="applyPromoCode()" class="bg-amber-600 hover:bg-amber-700 text-white font-bold px-4 py-2 rounded-xl text-xs shadow">تطبيق</button>
                </div>
                ${state.appliedDiscount ? `<div class="text-xs text-emerald-600 font-bold mt-2">✓ تم تطبيق الخصم (${state.appliedDiscount.code})</div>` : ''}
              </div>

              <div class="space-y-3 text-sm border-t border-gray-100 pt-4">
                <div class="flex justify-between text-gray-600">
                  <span>المجموع الفرعي:</span>
                  <span class="font-en text-gray-900 font-bold">${subtotal} EGP</span>
                </div>

                ${discount > 0 ? `
                  <div class="flex justify-between text-emerald-600">
                    <span>الخصم المطبق:</span>
                    <span class="font-en font-bold">-${discount} EGP</span>
                  </div>
                ` : ''}

                <div class="flex justify-between text-gray-500 text-xs">
                  <span>مصاريف الشحن:</span>
                  <span>تحدد في الخطوة التالية</span>
                </div>

                <div class="flex justify-between text-gray-900 font-black text-lg border-t border-gray-100 pt-3">
                  <span>الإجمالي الفرعي:</span>
                  <span class="text-amber-600 font-en">${grandTotal} EGP</span>
                </div>
              </div>

              <button onclick="navigateTo('checkout')" class="w-full bg-amber-600 hover:bg-amber-700 text-white font-black py-3.5 rounded-xl text-sm uppercase transition shadow-md">
                متابعة إتمام الطلب <i class="fas fa-arrow-left mr-1"></i>
              </button>
            </div>
          </div>
        ` : `
          <div class="text-center py-20 bg-white border border-gray-200 rounded-2xl shadow-sm">
            <i class="fas fa-shopping-cart text-5xl text-gray-300 mb-4"></i>
            <h2 class="text-xl font-bold text-gray-800">سلة التسوق فارغة حالياً</h2>
            <p class="text-gray-500 text-sm mt-1 mb-6">استعرض أفضل المكملات الغذائية وأضفها لسلتك الآن</p>
            <button onclick="navigateTo('shop')" class="bg-amber-600 text-white font-bold px-6 py-3 rounded-xl text-sm shadow">تصفح المنتجات</button>
          </div>
        `}
      `;

      return div;
    }

    function applyPromoCode() {
      const codeInput = document.getElementById('promo-code-input').value.trim().toUpperCase();
      const promo = state.data.discounts.find(d => d.code === codeInput && d.active);

      if (!promo) {
        showToast("كود الخصم غير صالح أو انتهت صلاحيته", "error");
        return;
      }

      if (state.getCartSubtotal() < promo.minOrder) {
        showToast(`هذا الكود يتطلب حداً أدنى للشراء قدره ${promo.minOrder} EGP`, "error");
        return;
      }

      state.appliedDiscount = promo;
      showToast("تم تطبيق الخصم بنجاح!", "success");
      renderApp();
    }

    // 6. Checkout View
    function renderCheckoutView() {
      const div = document.createElement('div');
      div.className = "max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-10";

      const subtotal = state.getCartSubtotal();
      const discount = state.getDiscountAmount();
      
      let selectedZone = state.data.shippingZones[0];
      let shippingCost = selectedZone.cost;
      if (subtotal >= state.data.store.freeShippingThreshold) {
        shippingCost = 0;
      }

      div.innerHTML = `
        <h1 class="text-3xl font-black text-gray-900 mb-8">إتمام الطلب والشحن</h1>

        <form id="checkout-form" onsubmit="handleOrderSubmission(event)" class="grid grid-cols-1 md:grid-cols-2 gap-8">
          <!-- Customer Shipping Details -->
          <div class="bg-white border border-gray-200 p-6 rounded-2xl space-y-4 shadow-sm">
            <h2 class="font-bold text-lg text-gray-900 border-b border-gray-100 pb-3">بيانات التوصيل</h2>

            <div>
              <label class="block text-xs font-bold text-gray-700 uppercase mb-1">الاسم بالكامل *</label>
              <input type="text" id="cust-name" required class="w-full bg-gray-50 border border-gray-200 text-gray-900 rounded-xl p-2.5 text-sm focus:outline-none focus:border-amber-500">
            </div>

            <div>
              <label class="block text-xs font-bold text-gray-700 uppercase mb-1">رقم الهاتف (واتساب) *</label>
              <input type="tel" id="cust-phone" required placeholder="010XXXXXXXX" class="w-full bg-gray-50 border border-gray-200 text-gray-900 rounded-xl p-2.5 text-sm focus:outline-none focus:border-amber-500 font-en">
            </div>

            <div>
              <label class="block text-xs font-bold text-gray-700 uppercase mb-1">المحافظة *</label>
              <select id="cust-gov" onchange="updateShippingCost(this.value)" class="w-full bg-gray-50 border border-gray-200 text-gray-900 rounded-xl p-2.5 text-sm focus:outline-none">
                ${state.data.shippingZones.map(z => `<option value="${z.governorate}">${z.governorate} (${z.cost} EGP)</option>`).join('')}
              </select>
            </div>

            <div>
              <label class="block text-xs font-bold text-gray-700 uppercase mb-1">المدينة / المنطقة *</label>
              <input type="text" id="cust-city" required class="w-full bg-gray-50 border border-gray-200 text-gray-900 rounded-xl p-2.5 text-sm focus:outline-none focus:border-amber-500">
            </div>

            <div>
              <label class="block text-xs font-bold text-gray-700 uppercase mb-1">العنوان بالتفصيل *</label>
              <textarea id="cust-address" required rows="2" placeholder="اسم الشارع، رقم العمارة، رقم الشقة" class="w-full bg-gray-50 border border-gray-200 text-gray-900 rounded-xl p-2.5 text-sm focus:outline-none focus:border-amber-500"></textarea>
            </div>

            <div>
              <label class="block text-xs font-bold text-gray-700 uppercase mb-1">طريقة الدفع *</label>
              <div class="space-y-2">
                <label class="flex items-center gap-3 p-3 bg-amber-50 border border-amber-300 rounded-xl cursor-pointer">
                  <input type="radio" name="paymentMethod" value="COD" checked class="accent-amber-600">
                  <span class="text-sm font-bold text-gray-900"><i class="fas fa-money-bill-wave text-amber-600 ml-2"></i>الدفع عند الاستلام (COD)</span>
                </label>
                <label class="flex items-center gap-3 p-3 bg-gray-50 border border-gray-200 rounded-xl cursor-pointer opacity-60">
                  <input type="radio" name="paymentMethod" value="ONLINE" disabled class="accent-amber-600">
                  <span class="text-sm font-bold text-gray-600"><i class="fas fa-credit-card text-gray-400 ml-2"></i>بطاقة إلكترونية / فوري (مغلق مؤقتاً)</span>
                </label>
              </div>
            </div>
          </div>

          <!-- Final Summary -->
          <div class="bg-white border border-gray-200 p-6 rounded-2xl space-y-6 h-fit shadow-sm">
            <h2 class="font-bold text-lg text-gray-900 border-b border-gray-100 pb-3">ملخص الفاتورة Final Order</h2>

            <div class="space-y-3 text-sm">
              <div class="flex justify-between text-gray-600">
                <span>إجمالي المنتجات:</span>
                <span class="font-en text-gray-900 font-bold">${subtotal} EGP</span>
              </div>

              ${discount > 0 ? `
                <div class="flex justify-between text-emerald-600">
                  <span>الخصم:</span>
                  <span class="font-en font-bold">-${discount} EGP</span>
                </div>
              ` : ''}

              <div class="flex justify-between text-gray-600">
                <span>تكلفة الشحن:</span>
                <span id="shipping-cost-display" class="font-en text-gray-900 font-bold">${shippingCost} EGP</span>
              </div>

              <div class="flex justify-between text-gray-900 font-black text-xl border-t border-gray-100 pt-4">
                <span>الإجمالي النهائي:</span>
                <span id="grand-total-display" class="text-amber-600 font-en">${Math.max(0, subtotal - discount + shippingCost)} EGP</span>
              </div>
            </div>

            <button type="submit" class="w-full bg-amber-600 hover:bg-amber-700 text-white font-black py-4 rounded-xl text-base transition uppercase shadow-lg shadow-amber-600/20">
              تأكيد الطلب الآن <i class="fas fa-check-circle mr-1"></i>
            </button>
          </div>
        </form>
      `;

      return div;
    }

    function updateShippingCost(govName) {
      const zone = state.data.shippingZones.find(z => z.governorate === govName);
      const subtotal = state.getCartSubtotal();
      const discount = state.getDiscountAmount();
      
      let cost = zone ? zone.cost : 60;
      if (subtotal >= state.data.store.freeShippingThreshold) {
        cost = 0;
      }

      document.getElementById('shipping-cost-display').innerText = `${cost} EGP`;
      document.getElementById('grand-total-display').innerText = `${Math.max(0, subtotal - discount + cost)} EGP`;
    }

    function handleOrderSubmission(e) {
      e.preventDefault();

      const name = document.getElementById('cust-name').value;
      const phone = document.getElementById('cust-phone').value;
      const gov = document.getElementById('cust-gov').value;
      const city = document.getElementById('cust-city').value;
      const address = document.getElementById('cust-address').value;

      const subtotal = state.getCartSubtotal();
      const discount = state.getDiscountAmount();
      const zone = state.data.shippingZones.find(z => z.governorate === gov);
      let shippingCost = zone ? zone.cost : 60;
      if (subtotal >= state.data.store.freeShippingThreshold) shippingCost = 0;

      const grandTotal = Math.max(0, subtotal - discount + shippingCost);

      const newOrder = {
        id: `EGO-${Math.floor(1000 + Math.random() * 9000)}-${Math.floor(100 + Math.random() * 900)}`,
        customerName: name,
        customerPhone: phone,
        governorate: gov,
        city,
        address,
        total: grandTotal,
        paymentMethod: "COD",
        paymentStatus: "في انتظار الدفع عند الاستلام",
        orderStatus: "قيد التحضير",
        date: new Date().toISOString().split('T')[0],
        items: [...state.cart]
      };

      // Deduct inventory
      state.cart.forEach(cartItem => {
        const prod = state.data.products.find(p => p.id === cartItem.productId);
        if (prod) prod.stock = Math.max(0, prod.stock - cartItem.qty);
      });

      state.data.orders.unshift(newOrder);
      state.lastCreatedOrder = newOrder;
      state.clearCart();
      state.save();

      navigateTo('order-success');
    }

    // 7. Order Success View
    function renderOrderSuccessView() {
      const div = document.createElement('div');
      div.className = "max-w-2xl mx-auto px-4 py-16 text-center space-y-6";

      const order = state.lastCreatedOrder;

      div.innerHTML = `
        <div class="w-20 h-20 bg-emerald-50 text-emerald-600 rounded-full flex items-center justify-center mx-auto text-4xl border border-emerald-200 shadow-sm">
          <i class="fas fa-check"></i>
        </div>

        <h1 class="text-3xl font-black text-gray-900">تم استلام طلبك بنجاح! 🎉</h1>
        <p class="text-gray-600 text-sm">رقم الطلب الخاص بك هو: <span class="font-bold text-amber-600 font-en">${order?.id}</span></p>

        <div class="bg-white border border-gray-200 p-6 rounded-2xl text-right space-y-3 text-sm shadow-sm">
          <div class="font-bold text-gray-900 border-b border-gray-100 pb-2">تفاصيل الطلب:</div>
          <div><span class="text-gray-500">الاسم:</span> <span class="text-gray-900 font-bold">${order?.customerName}</span></div>
          <div><span class="text-gray-500">العنوان:</span> <span class="text-gray-900">${order?.address} - ${order?.city} (${order?.governorate})</span></div>
          <div><span class="text-gray-500">الإجمالي النهائي:</span> <span class="text-amber-600 font-bold font-en">${order?.total} EGP</span></div>
        </div>

        <button onclick="navigateTo('home')" class="bg-amber-600 hover:bg-amber-700 text-white font-black px-8 py-3.5 rounded-xl text-sm transition uppercase shadow-md">
          العودة للصفحة الرئيسية
        </button>
      `;

      return div;
    }

    // 8. Admin View (/admin)
    function renderAdminView() {
      const div = document.createElement('div');
      div.className = "max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8";

      if (!state.adminLoggedIn) {
        div.innerHTML = `
          <div class="max-w-md mx-auto bg-white border border-gray-200 p-8 rounded-3xl space-y-6 shadow-md">
            <div class="text-center">
              <div class="w-12 h-12 bg-amber-600 text-white font-black text-2xl flex items-center justify-center rounded-xl mx-auto mb-2 font-en shadow">E</div>
              <h1 class="text-2xl font-black text-gray-900">تسجيل دخول الأدمن</h1>
              <p class="text-gray-500 text-xs mt-1">لوحة التحكم الإدارية لـ EGO SUPPLEMENT</p>
            </div>

            <form onsubmit="handleAdminLogin(event)" class="space-y-4">
              <div>
                <label class="block text-xs font-bold text-gray-700 uppercase mb-1">البريد الإلكتروني</label>
                <input type="email" id="admin-email" required value="admin@egosupplement.com" class="w-full bg-gray-50 border border-gray-200 text-gray-900 rounded-xl p-2.5 text-sm focus:outline-none focus:border-amber-500 font-en">
              </div>

              <div>
                <label class="block text-xs font-bold text-gray-700 uppercase mb-1">كلمة المرور</label>
                <input type="password" id="admin-pass" required value="123456" class="w-full bg-gray-50 border border-gray-200 text-gray-900 rounded-xl p-2.5 text-sm focus:outline-none focus:border-amber-500 font-en">
              </div>

              <button type="submit" class="w-full bg-amber-600 hover:bg-amber-700 text-white font-black py-3 rounded-xl text-sm uppercase transition shadow">
                تسجيل الدخول
              </button>
            </form>
          </div>
        `;
        return div;
      }

      // Calculated Stats
      const totalRevenue = state.data.orders.reduce((sum, o) => sum + o.total, 0);
      const totalOrders = state.data.orders.length;
      const lowStockCount = state.data.products.filter(p => p.stock <= 5).length;

      div.innerHTML = `
        <div class="flex justify-between items-center mb-8 border-b border-gray-200 pb-4">
          <div>
            <h1 class="text-2xl font-black text-gray-900">لوحة التحكم الإدارية (Admin)</h1>
            <p class="text-gray-500 text-xs mt-1">إدارة كاملة للمتجر والمنتجات والمخزون</p>
          </div>

          <button onclick="state.adminLoggedIn = false; renderApp();" class="text-xs bg-gray-100 hover:bg-gray-200 text-gray-700 px-3 py-2 rounded-xl border border-gray-300">
            <i class="fas fa-sign-out-alt ml-1"></i> خروج
          </button>
        </div>

        <!-- Navigation Tabs -->
        <div class="flex gap-2 border-b border-gray-200 mb-6 overflow-x-auto pb-2">
          <button onclick="state.adminTab = 'dashboard'; renderApp();" class="px-4 py-2 rounded-xl text-xs font-bold ${state.adminTab === 'dashboard' ? 'bg-amber-600 text-white shadow-sm' : 'text-gray-600 hover:bg-gray-100'}">الرئيسية والاحصائيات</button>
          <button onclick="state.adminTab = 'products'; renderApp();" class="px-4 py-2 rounded-xl text-xs font-bold ${state.adminTab === 'products' ? 'bg-amber-600 text-white shadow-sm' : 'text-gray-600 hover:bg-gray-100'}">إدارة المنتجات</button>
          <button onclick="state.adminTab = 'orders'; renderApp();" class="px-4 py-2 rounded-xl text-xs font-bold ${state.adminTab === 'orders' ? 'bg-amber-600 text-white shadow-sm' : 'text-gray-600 hover:bg-gray-100'}">الطلبات (${totalOrders})</button>
          <button onclick="state.adminTab = 'discounts'; renderApp();" class="px-4 py-2 rounded-xl text-xs font-bold ${state.adminTab === 'discounts' ? 'bg-amber-600 text-white shadow-sm' : 'text-gray-600 hover:bg-gray-100'}">كوبونات الخصم</button>
        </div>

        <!-- Tab Dynamic Content -->
        ${state.adminTab === 'dashboard' ? renderAdminDashboardTab(totalRevenue, totalOrders, lowStockCount) : ''}
        ${state.adminTab === 'products' ? renderAdminProductsTab() : ''}
        ${state.adminTab === 'orders' ? renderAdminOrdersTab() : ''}
        ${state.adminTab === 'discounts' ? renderAdminDiscountsTab() : ''}
      `;

      return div;
    }

    function handleAdminLogin(e) {
      e.preventDefault();
      state.adminLoggedIn = true;
      showToast("تم تسجيل دخول الأدمن بنجاح!", "success");
      renderApp();
    }

    function renderAdminDashboardTab(revenue, ordersCount, lowStock) {
      return `
        <div class="space-y-6">
          <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div class="bg-white border border-gray-200 p-6 rounded-2xl shadow-sm">
              <div class="text-xs text-gray-500 font-bold uppercase">إجمالي المبيعات</div>
              <div class="text-3xl font-black text-amber-600 font-en mt-2">${revenue.toLocaleString()} EGP</div>
            </div>

            <div class="bg-white border border-gray-200 p-6 rounded-2xl shadow-sm">
              <div class="text-xs text-gray-500 font-bold uppercase">إجمالي الطلبات</div>
              <div class="text-3xl font-black text-gray-900 font-en mt-2">${ordersCount}</div>
            </div>

            <div class="bg-white border border-gray-200 p-6 rounded-2xl shadow-sm">
              <div class="text-xs text-gray-500 font-bold uppercase">منتجات منخفضة المخزون</div>
              <div class="text-3xl font-black text-red-600 font-en mt-2">${lowStock}</div>
            </div>
          </div>
        </div>
      `;
    }

    function renderAdminProductsTab() {
      return `
        <div class="space-y-6">
          <div class="flex justify-between items-center">
            <h2 class="font-bold text-gray-900 text-lg">كتالوج المنتجات الحالية</h2>
            <button onclick="addNewProductPrompt()" class="bg-amber-600 hover:bg-amber-700 text-white font-bold px-4 py-2 rounded-xl text-xs shadow">+ إضافة منتج جديد</button>
          </div>

          <div class="bg-white border border-gray-200 rounded-2xl overflow-x-auto shadow-sm">
            <table class="w-full text-right text-sm">
              <thead class="bg-gray-50 text-gray-600 text-xs border-b border-gray-200">
                <tr>
                  <th class="p-4">المنتج</th>
                  <th class="p-4">SKU</th>
                  <th class="p-4">السعر</th>
                  <th class="p-4">المخزون</th>
                  <th class="p-4">إجراءات</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-gray-100 text-gray-800">
                ${state.data.products.map(p => `
                  <tr>
                    <td class="p-4 flex items-center gap-3">
                      <img src="${p.image}" class="w-10 h-10 object-cover rounded-lg bg-gray-50 border border-gray-200">
                      <span class="font-bold">${p.name}</span>
                    </td>
                    <td class="p-4 font-en text-xs text-gray-500">${p.sku}</td>
                    <td class="p-4 font-en text-amber-600 font-bold">${p.price} EGP</td>
                    <td class="p-4"><span class="${p.stock <= 5 ? 'text-red-600 font-bold' : ''}">${p.stock} قطعة</span></td>
                    <td class="p-4">
                      <button onclick="deleteProduct('${p.id}')" class="text-red-500 hover:text-red-700 p-1"><i class="fas fa-trash"></i></button>
                    </td>
                  </tr>
                `).join('')}
              </tbody>
            </table>
          </div>
        </div>
      `;
    }

    function addNewProductPrompt() {
      const name = prompt("اسم المنتج الجديد:");
      if (!name) return;
      const price = parseFloat(prompt("السعر (بالجنيه المصري):", "1500"));
      const stock = parseInt(prompt("الكمية المتوفرة بمخزون الأدمن:", "10"));

      const newProd = {
        id: `prod-${Date.now()}`,
        sku: `EGO-NEW-${Math.floor(100 + Math.random() * 900)}`,
        name,
        category: "protein",
        brand: "EGO SUPPLEMENT",
        price: price || 1000,
        oldPrice: null,
        stock: stock || 10,
        rating: 5.0,
        reviewsCount: 1,
        badge: "جديد",
        isFeatured: true,
        image: "https://images.unsplash.com/photo-1593095948071-474c5cc2989d?w=600&auto=format&fit=crop&q=80",
        flavors: ["شوكولاتة"],
        sizes: ["1 كجم"],
        description: "وصف منتج مكمل جديد مضاف من لوحة التحكم.",
        ingredients: "Pure Formulations.",
        nutrition: "Standard Protein Nutrition."
      };

      state.data.products.unshift(newProd);
      state.save();
      showToast("تم إضافة المنتج الجديد بنجاح!", "success");
      renderApp();
    }

    function deleteProduct(id) {
      if (confirm("هل أنت تأكد من رغبتك في حذف هذا المنتج من الكتالوج؟")) {
        state.data.products = state.data.products.filter(p => p.id !== id);
        state.save();
        showToast("تم حذف المنتج", "info");
        renderApp();
      }
    }

    function renderAdminOrdersTab() {
      return `
        <div class="bg-white border border-gray-200 rounded-2xl overflow-x-auto shadow-sm">
          <table class="w-full text-right text-sm">
            <thead class="bg-gray-50 text-gray-600 text-xs border-b border-gray-200">
              <tr>
                <th class="p-4">رقم الطلب</th>
                <th class="p-4">العميل</th>
                <th class="p-4">المحافظة</th>
                <th class="p-4">الإجمالي</th>
                <th class="p-4">الحالة</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-100 text-gray-800">
              ${state.data.orders.map(o => `
                <tr>
                  <td class="p-4 font-en font-bold text-amber-600">${o.id}</td>
                  <td class="p-4">${o.customerName} (${o.customerPhone})</td>
                  <td class="p-4">${o.governorate}</td>
                  <td class="p-4 font-en font-bold">${o.total} EGP</td>
                  <td class="p-4"><span class="bg-amber-100 text-amber-800 text-xs font-bold px-2.5 py-1 rounded-lg">${o.orderStatus}</span></td>
                </tr>
              `).join('')}
            </tbody>
          </table>
        </div>
      `;
    }

    function renderAdminDiscountsTab() {
      return `
        <div class="space-y-6">
          <div class="flex justify-between items-center">
            <h2 class="font-bold text-gray-900 text-lg">كوبونات الخصم المتاحة</h2>
            <button onclick="addPromoPrompt()" class="bg-amber-600 hover:bg-amber-700 text-white font-bold px-4 py-2 rounded-xl text-xs shadow">+ إضافة كود خصم</button>
          </div>

          <div class="bg-white border border-gray-200 rounded-2xl overflow-x-auto shadow-sm">
            <table class="w-full text-right text-sm">
              <thead class="bg-gray-50 text-gray-600 text-xs border-b border-gray-200">
                <tr>
                  <th class="p-4">الكود</th>
                  <th class="p-4">النوع</th>
                  <th class="p-4">القيمة</th>
                  <th class="p-4">الحد الأدنى للشراء</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-gray-100 text-gray-800">
                ${state.data.discounts.map(d => `
                  <tr>
                    <td class="p-4 font-en font-bold text-amber-600">${d.code}</td>
                    <td class="p-4">${d.type}</td>
                    <td class="p-4 font-en font-bold">${d.value} ${d.type === 'PERCENTAGE' ? '%' : 'EGP'}</td>
                    <td class="p-4 font-en">${d.minOrder} EGP</td>
                  </tr>
                `).join('')}
              </tbody>
            </table>
          </div>
        </div>
      `;
    }

    function addPromoPrompt() {
      const code = prompt("أدخل كود الخصم الجديد (مثال: EGO20):");
      if (!code) return;
      const value = parseFloat(prompt("قيمة الخصم (نسبة مئوية):", "20"));

      state.data.discounts.push({
        code: code.toUpperCase(),
        type: "PERCENTAGE",
        value: value || 10,
        minOrder: 500,
        active: true
      });
      state.save();
      showToast("تم إضافة كود الخصم الجديد!", "success");
      renderApp();
    }

    // 9. Footer Component
    function renderFooter() {
      const footer = document.createElement('footer');
      footer.className = "bg-white border-t border-gray-200 text-gray-600 text-sm py-12 shadow-sm";

      footer.innerHTML = `
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
          <div class="space-y-4">
            <div class="flex items-center gap-2">
              <div class="w-8 h-8 bg-amber-600 text-white font-black text-xl flex items-center justify-center rounded-lg font-en shadow">E</div>
              <span class="font-black text-xl text-gray-900 font-en tracking-wider">EGO<span class="text-amber-600">.</span></span>
            </div>
            <p class="text-xs text-gray-500 leading-relaxed">العلامة التجارية الأولى للمكملات الغذائية الرياضية عالية النقاء في مصر.</p>
          </div>

          <div>
            <h4 class="font-bold text-gray-900 text-xs uppercase mb-3 tracking-wider">روابط سريعة</h4>
            <ul class="space-y-2 text-xs">
              <li><button onclick="navigateTo('shop')" class="hover:text-amber-600 transition">كتالوج المنتجات</button></li>
              <li><button onclick="navigateTo('cart')" class="hover:text-amber-600 transition">سلة الشراء</button></li>
              <li><button onclick="navigateTo('admin')" class="hover:text-amber-600 transition">لوحة تحكم الأدمن</button></li>
            </ul>
          </div>

          <div>
            <h4 class="font-bold text-gray-900 text-xs uppercase mb-3 tracking-wider">تواصل معنا</h4>
            <ul class="space-y-2 text-xs font-en">
              <li><i class="fas fa-phone text-amber-600 ml-2"></i> ${state.data.store.phone}</li>
              <li><i class="fas fa-envelope text-amber-600 ml-2"></i> ${state.data.store.email}</li>
            </ul>
          </div>

          <div>
            <h4 class="font-bold text-gray-900 text-xs uppercase mb-3 tracking-wider">وسائل الدفع المقبولة</h4>
            <div class="flex items-center gap-3 text-2xl text-gray-400">
              <i class="fas fa-money-bill-wave text-amber-600"></i>
              <i class="fab fa-cc-visa"></i>
              <i class="fab fa-cc-mastercard"></i>
            </div>
          </div>
        </div>

        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 border-t border-gray-100 pt-6 text-center text-xs text-gray-400 font-en">
          &copy; 2026 EGO SUPPLEMENT. All Rights Reserved.
        </div>
      `;

      return footer;
    }

    // Router Navigation Handler
    function navigateTo(view, params = {}) {
      state.currentView = view;
      if (params.category) state.filterCategory = params.category;
      if (params.id) state.selectedProductId = params.id;
      window.scrollTo({ top: 0, behavior: 'smooth' });
      renderApp();
    }

    // Initialize Application
    window.onload = function() {
      renderApp();
    };
  </script>
</body>
</html>
