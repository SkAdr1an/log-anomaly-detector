import 'package:flutter/material.dart';
import 'ui/screens/welcome_screen.dart';
import 'ui/screens/style_selector_screen.dart';
import 'ui/screens/result_screen.dart';

final Map<String, WidgetBuilder> appRoutes = {
  '/': (context) => const WelcomeScreen(),
  '/styleselector': (context) => const StyleSelectorScreen(),
  '/result': (context) => const ResultScreen(),

  // As rotas abaixo foram comentadas porque os arquivos e classes não existem:
  // '/avatar_preview_negro': (context) =>
  //     const AvatarPreviewScreen(glbPath: 'assets/models/avatar_negro.glb'),
  // '/avatar_carousel': (context) => const AvatarCarouselScreen(),
};
