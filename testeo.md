# Testeo — Luján Homes

> Checklist técnico antes de lanzar. Verificación preliminar sobre el boceto actual
> (22/06/2026); se completa en la fase 4, tras aplicar los cambios. Ref: `../ESTANDAR.md`.

## Núcleo universal (todo sitio)

- [x] Footer con **fecha dinámica por JS** (detectado `getFullYear`)
- [ ] **Responsive / mobile-first** (probar en pantalla chica)
- [x] Metadatos para compartir: OG + Twitter Card (8 tags detectados — verificar `og:image`)
- [x] **Bloque destacado al portafolio** + crédito de autor (links a teocicciari detectados)
- [x] **Font Awesome** para los íconos
- [ ] Performance — `loading="lazy"` fuera del primer viewport  ⚠️ **0/13 imágenes con lazy: falta aplicarlo**
- [ ] Performance — fonts recortadas a los pesos usados (`display=swap`) — revisar
- [ ] Performance — Font Awesome self-host/recortado (no toda la CDN) — revisar
- [ ] Performance — `preload` de la imagen del hero — revisar

## Módulo hospedaje

- [x] **Formulario de reserva** con campos de fecha (`type="date"` detectado) — verificar los 4 campos: Nombre · Personas · Check-in · Check-out
- [ ] Campo `<select>` **Unidad** (Studio Deluxe / Suite Familiar Family / Loft) — recomendado dado que hay varias tipologías
- [ ] Validación check-out posterior a check-in
- [ ] Canal del form: WhatsApp (+54 9 11 5709 2992) — verificar `wa.me`

## Notas de testeo

- Verificación automática preliminar. Falta el testeo manual real (responsive en celular,
  envío del formulario, performance) que se hace en la fase 4, después de los cambios.
- Pendiente confirmado: aplicar `loading="lazy"` a las 13 imágenes.
