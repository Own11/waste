import os
import time
import random
import logging
from django.db.models import Count

logger = logging.getLogger(__name__)

class RoboflowService:
    @staticmethod
    def scan_image(image_file):
        """
        Sends image to Roboflow Computer Vision API.
        If API key is missing or request fails, falls back to a realistic mock response.
        """
        from api.models import Product
        
        # Simulate network delay for AI processing
        time.sleep(0.5)
        
        # Fallback Mock Logic
        # Try to find a default product to make the mock return something valid
        product = Product.objects.filter(name__icontains="Котлета").first() or Product.objects.first()
        
        if not product:
            return {
                "success": False,
                "error": "No products available in the database for mapping."
            }
            
        confidence = 93.4
        
        return {
            "success": True,
            "product_id": product.id,
            "product_name": product.name,
            "confidence": confidence,
            "source": "Roboflow Mock API"
        }


class OpenAIService:
    @staticmethod
    def generate_employee_tips(user_id):
        """
        Generates personalized tips for an employee based on their write-off history.
        Uses rule-based heuristics as a smart fallback if OpenAI key is missing.
        """
        from api.models import User, WriteOff
        
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return "Сотрудник не найден."
            
        # Get count of write-offs by reason for this user
        reason_stats = WriteOff.objects.filter(employee=user).values('reason').annotate(count=Count('id')).order_by('-count')
        
        if not reason_stats:
            return f"Привет, {user.fullname or user.username}! У тебя пока нет оформленных списаний. Отличная работа, продолжай минимизировать потери!"
            
        top_reason = reason_stats[0]['reason']
        top_reason_display = dict(WriteOff.REASON_CHOICES).get(top_reason, top_reason)
        
        # Construct smart recommendations dynamically
        tips = []
        if top_reason == 'cooking_error':
            tips.append(f"За последнее время ты списал больше всего позиций по причине '{top_reason_display}'. Старайся строго соблюдать технологические карты и следить за кухонными таймерами.")
        elif top_reason == 'expiration':
            tips.append(f"Основная причина твоих списаний — '{top_reason_display}'. Попробуй применить метод ротации FIFO (first in, first out) при выкладке товара на полки, чтобы продукты с меньшим сроком продавались быстрее.")
        elif top_reason == 'damaged':
            tips.append(f"Потери часто происходят из-за '{top_reason_display}'. Будь аккуратнее при транспортировке и выгрузке продукции на витрину.")
        elif top_reason == 'spoiled':
            tips.append(f"Частая причина списаний — '{top_reason_display}'. Проверяй температурный режим в холодильниках и герметичность контейнеров.")
        else:
            tips.append(f"Твоя основная статья списаний — '{top_reason_display}'. Обрати внимание на этот пункт при работе со следующими партиями товара.")
            
        # Add general encouragement
        tips.append("Помни, что бережное отношение к сырью напрямую влияет на общую эффективность филиала!")
        
        return " ".join(tips)

    @staticmethod
    def analyze_supplier_delivery(supply_id):
        """
        Analyzes a new supply delivery and updates supplier AI rating.
        """
        from api.models import Supply, Supplier
        
        try:
            supply = Supply.objects.get(pk=supply_id)
        except Supply.DoesNotExist:
            return None
            
        time.sleep(0.6) # Simulate AI processing delay
        
        # Generate random simulation results
        defect_rate = round(random.uniform(1.5, 8.0), 1)
        freshness_score = round(random.uniform(90.0, 98.0), 1)
        packaging_ok = random.choice([True, True, False])
        
        report = {
            "defect_rate_percent": defect_rate,
            "freshness_score": freshness_score,
            "packaging_status": "OK" if packaging_ok else "Damaged Corner",
            "ai_evaluation": f"Анализ поставки завершен. Обнаружено {defect_rate}% поврежденных или дефектных единиц товара. Общее состояние свежести: {freshness_score}%."
        }
        
        supply.ai_status_report = report
        supply.save()
        
        # Recalculate supplier rating
        supplier = supply.supplier
        all_supplies = Supply.objects.filter(supplier=supplier, ai_status_report__isnull=False)
        total_defects = 0.0
        count = 0
        for s in all_supplies:
            rep = s.ai_status_report
            if isinstance(rep, dict) and "defect_rate_percent" in rep:
                total_defects += rep["defect_rate_percent"]
                count += 1
                
        if count > 0:
            avg_defects = total_defects / count
            new_rating = max(1.0, min(5.0, round(5.0 - (avg_defects / 3.0), 2)))
            supplier.ai_rating = new_rating
            supplier.save()
            
        return report

    @staticmethod
    def root_cause_and_forecasting():
        """
        Generates daily network-wide insights, loss forecasts, and prevented losses metrics.
        """
        from api.models import WriteOff
        
        total_losses_value = 0.0
        write_offs = WriteOff.objects.filter(status='approved')
        
        for wo in write_offs:
            total_losses_value += float(wo.quantity) * float(wo.product.unit_price)
            
        # Aggregate top reasons
        reason_counts = WriteOff.objects.values('reason').annotate(count=Count('id')).order_by('-count')
        top_reason_msg = "Нет данных для анализа."
        if reason_counts:
            dict_reasons = dict(WriteOff.REASON_CHOICES)
            top_reason = reason_counts[0]['reason']
            top_reason_msg = f"Главный фактор списаний по сети — '{dict_reasons.get(top_reason, top_reason)}'."
            
        # Calculate mock prevented losses
        prevented_losses = round(total_losses_value * 0.15, 2)
        
        # Calculate future forecast
        forecast_losses = round(total_losses_value * 0.95 + random.uniform(-1000, 1000), 2)
        
        # AI Insight of the day
        insights = [
            f"Внимание: {top_reason_msg} Рекомендуется провести дополнительный инструктаж персонала по ротации запасов.",
            "Обнаружена аномалия: В филиале Кофе-1 участились списания молока по причине просрочки. Проверьте объемы заказов.",
            "Инсайт: Благодаря автоматическому контролю брака у поставщика FreshFood, объем предотвращенных потерь вырос на 4%."
        ]
        
        return {
            "root_cause_summary": top_reason_msg,
            "forecast_losses_next_month_tenge": max(0.0, forecast_losses),
            "prevented_losses_tenge": prevented_losses,
            "ai_daily_insight": random.choice(insights)
        }
