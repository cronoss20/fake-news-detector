# 🚀 Guía de Demo en Vivo - Detector de Noticias Falsas

[English Version](QUICKSTART.md) | **Versión en Español**

Esta guía proporciona instrucciones completas para desplegar una demo en vivo del Detector de Noticias Falsas.

## 📋 Índice

- [Acerca del Proyecto](#acerca-del-proyecto)
- [Opciones de Despliegue](#opciones-de-despliegue)
- [Despliegue Rápido (5 minutos)](#despliegue-rápido-5-minutos)
- [Seguridad y Privacidad](#seguridad-y-privacidad)
- [Recursos Adicionales](#recursos-adicionales)

## 🔍 Acerca del Proyecto

El Detector de Noticias Falsas es una aplicación web completa que analiza contenido de texto y URLs para identificar posible desinformación usando el modelo GPT de OpenAI.

### Características Principales

- **Análisis de Texto**: Los usuarios pueden pegar texto sospechoso directamente
- **Análisis de URL**: Los usuarios pueden ingresar URLs de artículos de noticias
- **Modo Demo**: Funciona sin necesidad de clave API usando análisis heurístico
- **Modo AI**: Análisis avanzado con GPT-3.5-turbo (requiere clave API de OpenAI)
- **Interfaz Moderna**: Diseño responsivo que funciona en todos los dispositivos

## 🚀 Opciones de Despliegue

### Opción 1: Render.com (Recomendado - Más Fácil)

**Tiempo: ~5 minutos | Costo: Gratis**

#### Despliegue del Backend

1. **Haz Fork** de este repositorio a tu cuenta de GitHub

2. Ve a [render.com](https://render.com) y regístrate (gratis)

3. Haz clic en **"New +"** → **"Web Service"**

4. Conecta tu repositorio de GitHub

5. Configura:
   ```
   Nombre: fake-news-detector-backend
   Entorno: Python 3
   Comando de Construcción: cd backend && pip install -r requirements.txt
   Comando de Inicio: cd backend && python app.py
   ```

6. Agrega Variable de Entorno (opcional):
   ```
   OPENAI_API_KEY = tu_clave_api_aqui
   ```

7. Haz clic en **"Create Web Service"**

8. **Copia tu URL del backend** (ej: `https://fake-news-detector-backend.onrender.com`)

#### Despliegue del Frontend

1. En Render, haz clic en **"New +"** → **"Static Site"**

2. Selecciona tu repositorio nuevamente

3. Configura:
   ```
   Nombre: fake-news-detector-frontend
   Comando de Construcción: cd frontend && npm install && npm run build
   Directorio de Publicación: frontend/build
   ```

4. Agrega Variable de Entorno:
   ```
   REACT_APP_BACKEND_URL = [tu URL del backend del paso 8]
   ```

5. Haz clic en **"Create Static Site"**

6. **¡Listo!** Tu URL del frontend será mostrada

### Opción 2: Railway.app

**Tiempo: ~5 minutos | Costo: Gratis**

1. Ve a [railway.app](https://railway.app) y regístrate
2. Haz clic en **"New Project"** → **"Deploy from GitHub repo"**
3. Selecciona tu repositorio
4. Railway detectará y desplegará automáticamente ambos servicios
5. Agrega variables de entorno:
   - Backend: `OPENAI_API_KEY` (opcional)
   - Frontend: `REACT_APP_BACKEND_URL`

### Opción 3: Vercel (Frontend) + Render (Backend)

**Tiempo: ~7 minutos | Costo: Gratis**

#### Backend en Render
Sigue los pasos de la Opción 1 para el backend.

#### Frontend en Vercel
1. Instala Vercel CLI: `npm install -g vercel`
2. Navega al directorio frontend: `cd frontend`
3. Despliega: `vercel --prod`
4. Configura la variable de entorno: `REACT_APP_BACKEND_URL`

## 🔒 Seguridad y Privacidad

### Protección de Datos del Usuario

✅ **Sin Almacenamiento de Datos**
- La aplicación NO almacena ningún contenido enviado por los usuarios
- Todo el análisis se realiza en memoria solamente
- Los resultados no se guardan en el servidor

✅ **Sin Registro de Contenido**
- Las entradas de los usuarios nunca se registran en archivos
- Solo se registran errores del sistema (sin contenido del usuario)
- No se recopila información personal identificable

✅ **Procesamiento Temporal**
- Cada solicitud es independiente y sin estado
- No hay seguimiento de sesión ni cookies
- No se requieren cuentas de usuario

### Seguridad de la Clave API

✅ **Variables de Entorno**
- La clave API de OpenAI se almacena de forma segura en variables de entorno
- Nunca se expone en el código del frontend
- Nunca se envía en las respuestas de la API

✅ **Modo Demo**
- La aplicación funciona sin clave API
- Usa análisis heurístico basado en palabras clave
- Proporciona funcionalidad inmediata sin configuración

### Medidas de Seguridad Recomendadas

1. ✅ Usar HTTPS para todo el tráfico de producción
2. ✅ Configurar CORS correctamente (no usar wildcard `*`)
3. ✅ Establecer límites de tasa para prevenir abuso
4. ✅ Mantener las dependencias actualizadas
5. ✅ Monitorear el uso y los costos de la API

Para más detalles de seguridad, consulta [SECURITY.md](SECURITY.md).

## ⚙️ Variables de Entorno

### Backend (.env)
```env
OPENAI_API_KEY=tu_clave_openai_aqui  # Opcional
FLASK_ENV=production
PORT=5000
```

### Frontend (.env)
```env
REACT_APP_BACKEND_URL=https://tu-url-backend.com
```

## 🧪 Probando tu Despliegue

### Verificación del Backend
```bash
curl https://tu-url-backend.com/
```
Respuesta esperada: `{"status": "Fake News Detector backend running."}`

### Verificación del Frontend
1. Visita tu URL del frontend
2. Prueba el análisis de texto con:
   ```
   NOTICIA DE ÚLTIMA HORA: ¡No vas a creer este descubrimiento chocante que los médicos odian!
   ```
3. Verifica que se muestren los resultados

### Lista de Verificación

- [ ] Backend accesible
- [ ] Frontend carga correctamente
- [ ] Análisis de texto funciona
- [ ] Análisis de URL funciona
- [ ] Manejo de errores funciona
- [ ] Diseño responsivo en móvil
- [ ] HTTPS habilitado

## 📚 Recursos Adicionales

### Documentación Completa

- **[QUICKSTART.md](QUICKSTART.md)** - Guía rápida en inglés
- **[DEMO.md](DEMO.md)** - Guía completa de despliegue (inglés)
- **[SECURITY.md](SECURITY.md)** - Mejores prácticas de seguridad (inglés)
- **[DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md)** - Lista de verificación (inglés)
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - Diagrama de arquitectura (inglés)

### Scripts de Despliegue Automatizado

```bash
# Despliegue en Render
./deploy/render-deploy.sh

# Despliegue en Railway
./deploy/railway-deploy.sh

# Despliegue en Vercel + Render
./deploy/vercel-render-deploy.sh
```

## 🆘 Solución de Problemas

### Problema: El backend no es accesible
**Solución:**
- Verifica que el backend esté en ejecución
- Comprueba las reglas del firewall
- Verifica que las variables de entorno estén configuradas correctamente

### Problema: El frontend no puede alcanzar el backend
**Solución:**
- Verifica que `REACT_APP_BACKEND_URL` esté configurado correctamente
- Comprueba la configuración de CORS en el backend
- Asegúrate de que la URL del backend sea accesible desde el navegador

### Problema: Errores de la API de OpenAI
**Solución:**
- Verifica que la clave API sea válida
- Comprueba la cuota y facturación de la API
- La aplicación volverá automáticamente al modo demo si falla la API

## 🎉 ¡Éxito!

Una vez desplegada, tu demo en vivo estará accesible en:
- **Frontend**: `https://tu-url-frontend.com`
- **Backend API**: `https://tu-url-backend.com`

### Próximos Pasos

1. ⭐ Marca este repositorio con una estrella
2. 🔗 Agrega tu URL de demo en vivo al README
3. 📢 Comparte en redes sociales
4. 🛡️ Revisa las mejores prácticas de seguridad
5. 📚 Lee la guía completa para opciones avanzadas

## 📊 Comparación de Plataformas

| Plataforma | Backend | Frontend | Gratis | Tiempo |
|------------|---------|----------|--------|--------|
| **Render** | ✅ | ✅ | ✅ Sí | ~5 min |
| **Railway** | ✅ | ✅ | ✅ Sí | ~5 min |
| **Vercel + Render** | ✅ | ✅ | ✅ Sí | ~7 min |
| **Netlify + Render** | ✅ | ✅ | ✅ Sí | ~7 min |

## 💡 Consejos

- Comienza con Render si eres principiante
- Usa Vercel + Render para mejor rendimiento
- Railway es excelente para desarrolladores
- Siempre usa HTTPS en producción
- Configura el monitoreo de tiempo de actividad
- Mantén las dependencias actualizadas

## 📞 Soporte

¿Necesitas ayuda?
- 📖 Consulta la documentación completa
- 🐛 Abre un issue en GitHub
- 💬 Revisa los issues existentes para soluciones

---

**¡Feliz despliegue!** 🚀

Desarrollado con ❤️ para ayudar a combatir la desinformación.
