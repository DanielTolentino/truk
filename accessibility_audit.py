#!/usr/bin/env python3
"""
Script de Auditoria de Acessibilidade para TruK
Verifica problemas comuns de acessibilidade nos templates HTML
"""

import os
import re
from pathlib import Path
from collections import defaultdict

class AccessibilityAuditor:
    def __init__(self, templates_dir):
        self.templates_dir = Path(templates_dir)
        self.issues = defaultdict(list)
        
    def audit_all(self):
        """Executa todas as verificações de acessibilidade"""
        print("🔍 Iniciando Auditoria de Acessibilidade\n")
        print("=" * 60)
        
        for template_file in self.templates_dir.rglob("*.html"):
            self.audit_file(template_file)
        
        self.print_report()
        
    def audit_file(self, file_path):
        """Audita um arquivo HTML específico"""
        rel_path = file_path.relative_to(self.templates_dir)
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Verificações
        self.check_lang_attribute(content, rel_path)
        self.check_images_alt(content, rel_path)
        self.check_form_labels(content, rel_path)
        self.check_headings_structure(content, rel_path)
        self.check_aria_attributes(content, rel_path)
        self.check_button_labels(content, rel_path)
        self.check_link_text(content, rel_path)
        self.check_table_headers(content, rel_path)
        self.check_color_only_info(content, rel_path)
        
    def check_lang_attribute(self, content, file_path):
        """Verifica se o atributo lang está presente no HTML"""
        if '<html' in content and 'lang=' not in content:
            self.issues['Sem atributo lang'].append(str(file_path))
    
    def check_images_alt(self, content, file_path):
        """Verifica se imagens têm texto alternativo"""
        img_pattern = r'<img[^>]*>'
        imgs = re.findall(img_pattern, content, re.IGNORECASE)
        
        for img in imgs:
            if 'alt=' not in img.lower():
                self.issues['Imagem sem alt text'].append(f"{file_path}: {img[:50]}...")
    
    def check_form_labels(self, content, file_path):
        """Verifica se inputs têm labels associados"""
        # Procura por inputs sem labels com for
        input_pattern = r'<input[^>]*>'
        inputs = re.findall(input_pattern, content, re.IGNORECASE)
        
        for input_tag in inputs:
            if 'type="hidden"' not in input_tag.lower() and 'type="submit"' not in input_tag.lower():
                # Verifica se tem id
                id_match = re.search(r'id=["\']([^"\']+)["\']', input_tag)
                if id_match:
                    input_id = id_match.group(1)
                    # Verifica se existe um label com for=input_id
                    if f'for="{input_id}"' not in content and f"for='{input_id}'" not in content:
                        self.issues['Input sem label explícito'].append(f"{file_path}: id={input_id}")
    
    def check_headings_structure(self, content, file_path):
        """Verifica estrutura de headings"""
        headings = re.findall(r'<h([1-6])[^>]*>', content, re.IGNORECASE)
        
        if headings:
            levels = [int(h) for h in headings]
            # Verifica se começa com h1
            if levels and levels[0] != 1:
                self.issues['Headings não começam com h1'].append(f"{file_path}: começa com h{levels[0]}")
            
            # Verifica pulos de níveis
            for i in range(len(levels) - 1):
                if levels[i+1] - levels[i] > 1:
                    self.issues['Pulo na hierarquia de headings'].append(
                        f"{file_path}: h{levels[i]} -> h{levels[i+1]}"
                    )
    
    def check_aria_attributes(self, content, file_path):
        """Verifica uso de ARIA attributes em elementos interativos"""
        # Dropdowns sem aria-expanded
        if 'dropdown' in content.lower():
            if 'aria-expanded' not in content.lower():
                self.issues['Dropdown sem aria-expanded'].append(str(file_path))
        
        # Modals sem aria-modal
        if 'modal' in content.lower():
            if 'aria-modal' not in content.lower() and 'role="dialog"' not in content.lower():
                self.issues['Modal sem aria-modal/role'].append(str(file_path))
    
    def check_button_labels(self, content, file_path):
        """Verifica se botões têm texto descritivo"""
        button_pattern = r'<button[^>]*>([^<]*)</button>'
        buttons = re.findall(button_pattern, content, re.IGNORECASE)
        
        for button_text in buttons:
            button_text = button_text.strip()
            # Remove variáveis Django
            button_text = re.sub(r'\{[^}]*\}', '', button_text).strip()
            if not button_text:
                self.issues['Botão sem texto descritivo'].append(str(file_path))
    
    def check_link_text(self, content, file_path):
        """Verifica texto de links genéricos"""
        generic_texts = ['clique aqui', 'aqui', 'leia mais', 'saiba mais']
        for text in generic_texts:
            if f'>{text}<' in content.lower():
                self.issues['Link com texto genérico'].append(f"{file_path}: '{text}'")
    
    def check_table_headers(self, content, file_path):
        """Verifica se tabelas têm headers apropriados"""
        if '<table' in content.lower():
            if '<th' not in content.lower():
                self.issues['Tabela sem headers (th)'].append(str(file_path))
            elif 'scope=' not in content.lower():
                self.issues['Tabela sem atributo scope'].append(str(file_path))
            
            if '<caption' not in content.lower():
                self.issues['Tabela sem caption'].append(str(file_path))
    
    def check_color_only_info(self, content, file_path):
        """Verifica uso de emojis/ícones sem texto alternativo"""
        # Emojis sem aria-label
        emoji_pattern = r'[🚚🚛📦✅🛣️💰🏆⚠️❌]'
        if re.search(emoji_pattern, content):
            # Verifica se tem aria-label próximo
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if re.search(emoji_pattern, line):
                    # Verifica contexto (3 linhas antes e depois)
                    context = '\n'.join(lines[max(0, i-3):min(len(lines), i+4)])
                    if 'aria-label' not in context and 'aria-hidden' not in context:
                        self.issues['Emoji sem aria-label'].append(f"{file_path}: linha ~{i+1}")
    
    def print_report(self):
        """Imprime relatório de problemas encontrados"""
        print("\n📊 RELATÓRIO DE ACESSIBILIDADE")
        print("=" * 60)
        
        if not self.issues:
            print("✅ Nenhum problema crítico encontrado!")
            return
        
        total_issues = sum(len(v) for v in self.issues.values())
        print(f"\n⚠️  Total de problemas encontrados: {total_issues}\n")
        
        # Ordena por categoria
        for category in sorted(self.issues.keys()):
            problems = self.issues[category]
            print(f"\n🔴 {category} ({len(problems)} ocorrências)")
            print("-" * 60)
            for problem in problems[:5]:  # Mostra até 5 exemplos
                print(f"   • {problem}")
            if len(problems) > 5:
                print(f"   ... e mais {len(problems) - 5} ocorrências")
        
        # Sumário por prioridade
        print("\n" + "=" * 60)
        print("📋 SUMÁRIO POR PRIORIDADE")
        print("=" * 60)
        
        critical = ['Input sem label explícito', 'Imagem sem alt text', 'Tabela sem headers (th)']
        high = ['Sem atributo lang', 'Dropdown sem aria-expanded', 'Botão sem texto descritivo']
        medium = ['Tabela sem caption', 'Emoji sem aria-label', 'Tabela sem atributo scope']
        
        print("\n🔴 CRÍTICO:")
        for issue in critical:
            if issue in self.issues:
                print(f"   • {issue}: {len(self.issues[issue])}")
        
        print("\n🟠 ALTO:")
        for issue in high:
            if issue in self.issues:
                print(f"   • {issue}: {len(self.issues[issue])}")
        
        print("\n🟡 MÉDIO:")
        for issue in medium:
            if issue in self.issues:
                print(f"   • {issue}: {len(self.issues[issue])}")
        
        print("\n" + "=" * 60)

if __name__ == "__main__":
    templates_dir = Path(__file__).parent / "templates"
    auditor = AccessibilityAuditor(templates_dir)
    auditor.audit_all()
    
    print("\n✨ Auditoria concluída!")
    print("\n💡 Próximos passos:")
    print("   1. Revisar e priorizar os problemas encontrados")
    print("   2. Corrigir problemas críticos primeiro")
    print("   3. Implementar melhorias incrementais")
    print("   4. Testar com screen readers (NVDA, JAWS, VoiceOver)")
    print("   5. Validar navegação por teclado")
